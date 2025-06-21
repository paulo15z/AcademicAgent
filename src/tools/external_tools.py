#----------------------------------------------------------------------#
# IMPORTAÇÃO DE BIBLIOTECAS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#

import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
import openai
import numpy as np
import os
from urllib.parse import quote
from bs4.element import Tag
#----------------------------------------------------------------------#
# OBTER DADOS DE HISTÓRICO DE PREÇO ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#

class PriceHistoryInput(BaseModel):
    ticker: str = Field(..., description="Símbolo do ativo (ex: AAPL, BTC-USD)")
    period: str = Field("1y", description="Período de coleta (ex: 1d, 5d, 1mo, 1y)")
    interval: str = Field("1d", description="Intervalo de tempo (ex: 1m, 1h, 1wk)")

class PriceHistoryOutput(BaseModel):
    data: List[Dict[str, Any]]

def get_price_history(input: PriceHistoryInput) -> PriceHistoryOutput:
    """
    Busca dados históricos de preço para um ativo específico.
    """
    try:
        df = yf.download(input.ticker, period=input.period, interval=input.interval, progress=False)
        if df is not None and not df.empty:
            df.reset_index(inplace=True)
            for col in df.columns:
                if col != "Date":
                    df[col] = df[col].astype(str)
            if df is not None:  # Explicit check for linter
                return PriceHistoryOutput(data=df.to_dict(orient="records"))
    except Exception as e:
        print(f"Erro ao buscar preços para {input.ticker}: {e}")
    return PriceHistoryOutput(data=[])

#----------------------------------------------------------------------#
# BUSCAR NOTÍCIAS RELEVANTES ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#

class RelevantNewsInput(BaseModel):
    """Input para buscar notícias relevantes de um ativo."""
    ticker: str = Field(..., description="Símbolo do ativo (ex: AAPL, BTC-USD)")

class NewsArticle(BaseModel):
    """Representa um único artigo de notícia."""
    title: str = Field(..., description="O título da notícia.")
    link: str = Field(..., description="O link para a notícia completa.")
    source: str = Field(..., description="A fonte da notícia (ex: Google News).")

class RelevantNewsOutput(BaseModel):
    """Output contendo uma lista de notícias relevantes."""
    articles: List[NewsArticle] = Field(..., description="Lista de artigos de notícias encontrados.")

def get_relevant_news(input: RelevantNewsInput) -> RelevantNewsOutput:
    articles = []
    try:
        ticker_info = yf.Ticker(input.ticker)
        company_name = ticker_info.info.get('longName', input.ticker)
    except Exception:
        company_name = input.ticker

    query = f"{input.ticker} {company_name}"
    url = f"https://news.google.com/rss/search?q={quote(query)}&hl=pt-BR&gl=BR&ceid=BR:pt-419"

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'xml')

        for item in soup.find_all('item')[:10]:
            try:
                title_tag = item.find('title')  # type: ignore
                link_tag = item.find('link')  # type: ignore

                title = title_tag.get_text(strip=True) if title_tag else "Sem título"  # type: ignore
                link = link_tag.get_text(strip=True) if link_tag else ""  # type: ignore

                articles.append(NewsArticle(title=title, link=link, source="Google News"))

            except (AttributeError, TypeError):
                continue

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar notícias para {input.ticker}: {e}")

    return RelevantNewsOutput(articles=articles)

#----------------------------------------------------------------------#
# CALCULAR INDICADORES TÉCNICOS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#

class IndicatorInput(BaseModel):
    """Input para calcular indicadores técnicos."""
    data: List[Dict[str, Any]] = Field(..., description="Histórico de preços com colunas como 'close')")

class IndicatorOutput(BaseModel):
    """Output contendo os indicadores calculados."""
    indicators: List[Dict[str, Any]] 

#----------------------------------------------------------------------#

class SMAInput(IndicatorInput):
    window: int = Field(20, description="Janela de cálculo da média (ex: 20 dias)")

def calculate_sma(input: SMAInput) -> IndicatorOutput:
    df= pd.DataFrame(input.data)
    df[f"SMA_{input.window}"] = df["Close"].rolling(window=input.window).mean()
    return IndicatorOutput(indicators=df.to_dict(orient="records"))

#-----------------------------------------------------------------------#

class RSIInput(IndicatorInput):
    period: int = Field(14, description="Número de períodos para o cálculo do RSI (ex: 14)")

def calculate_rsi(input: RSIInput) -> IndicatorOutput:
    df = pd.DataFrame(input.data)
    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=input.period).mean()
    avg_loss = loss.rolling(window=input.period).mean()
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return IndicatorOutput(indicators=df.to_dict(orient="records"))

#-----------------------------------------------------------------------#

class MACDInput(IndicatorInput):
    short_period: int = Field(12, description="Período da EMA curta")
    long_period: int = Field(26, description="Período da EMA longa")
    signal_period: int = Field(9, description="Período da linha de sinal")

def calculate_macd(input: MACDInput) -> IndicatorOutput:
    df = pd.DataFrame(input.data)
    df["EMA_short"] = df["Close"].ewm(span=input.short_period, adjust=False).mean()
    df["EMA_long"] = df["Close"].ewm(span=input.long_period, adjust=False).mean()
    df["MACD"] = df["EMA_short"] - df["EMA_long"]
    df["MACD_Signal"] = df["MACD"].ewm(span=input.signal_period, adjust=False).mean()
    return IndicatorOutput(indicators=df.to_dict(orient="records"))


#----------------------------------------------------------------------#
# ANALISAR SENTIMENTO DE NOTÍCIAS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#




#----------------------------------------------------------------------#
# ANALISAR SENTIMENTO DE NOTÍCIAS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#



#----------------------------------------------------------------------#
# SUMÁRIO GERAL DO ATIVO ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
# IMPORTAÇÃO DE BIBLIOTECAS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

#----------------------------------------------------------------------#
# DEFINIÇÃO DE SAÍDA ESTRUTURADA ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#----------------------------------------------------------------------#

class MarketAnalysisOutput(BaseModel):
    """
    Representa a saída estruturada da análise de mercado e sentimento de notícias pelo Agente de IA.
    """
    historical_price_trend: str = Field(
        description="Análise detalhada da tendência de preço histórica do ativo, incluindo pontos de alta, baixa e movimentos significativos."
    )
    news_perception: str = Field(
        description="As percepções e eventos principais extraídos das notícias recentes que podem ter impactado ou podem impactar o ativo."
    )
    sentiment_analysis: str = Field(
        description="Análise do sentimento geral (positivo, negativo ou neutro) das notícias indicando a polaridade dominante e justificativa."
    )

class MarketAnalysisDependencies(BaseModel):
    """
    Define as dependências de entrada para o Agente de Análise de Mercado.
    """
    symbol: str = Field(
        description="O símbolo do ativo financeiro a ser analisado (exemplo: 'AAPL', 'GOOG', 'TSLA')."
    )
   
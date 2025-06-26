Purpose: High-level vision, architecture, constraints, tech stack, tools, etc.
Prompt to AI: "Use the structure and decisions outlined in PLANNING.md."
Have the LLM reference this file at the beginning of any new conversation.


# PLANNING.md - AI Academic Agent Project

## Visão Geral do Projeto

Este projeto visa desenvolver um agente de IA (AI Agent) e um workflow inteligente para resolução, auxílio e formatação de atividades acadêmicas. O sistema será extensível, modular e focado em automação de tarefas acadêmicas como: geração de textos, revisão, formatação ABNT, sumarização, explicação de conceitos, entre outros.

## Propósito

Facilitar a vida de estudantes, professores e pesquisadores, automatizando processos repetitivos e fornecendo assistência inteligente para atividades acadêmicas, utilizando tecnologias de ponta em IA generativa e validação de dados.

## Objetivos do Projeto

### Objetivos Primários
- Desenvolver um agente de IA capaz de resolver e auxiliar em tarefas acadêmicas.
- Implementar workflows customizáveis para diferentes tipos de atividades (redação, revisão, formatação, etc).
- Integrar modelos de linguagem avançados (OpenAI GPT-4.1-nano agent).
- Garantir validação e estruturação dos dados com pydanticAI.
- Fornecer interface clara para extensão futura (ex: langgraphs, MCP server).

### Objetivos Secundários
- Suporte a múltiplos formatos de entrada/saída (texto, PDF, DOCX, etc).
- Ferramentas para sumarização, explicação, tradução e formatação acadêmica.
- Logging, monitoramento e testes automatizados.
- Documentação clara e exemplos práticos.

## Escopo do Projeto

### Incluído no Escopo
- Implementação do agente acadêmico principal.
- Workflows para tarefas acadêmicas comuns.
- Integração com OpenAI GPT-4.1-nano agent.
- Validação de dados com pydanticAI.
- Testes unitários e documentação.

### Fora do Escopo (Fase 1)
- Interface gráfica completa.
- Integração com sistemas acadêmicos externos.
- Suporte a múltiplos idiomas (além do português e inglês).
- Integração total com MCP server (planejado para o futuro).

## Arquitetura Proposta

### Componentes Principais
1. **Core Agent**: Núcleo do agente de IA e orquestração de workflows.
2. **Workflow Manager**: Gerenciamento de fluxos de tarefas acadêmicas.
3. **Data Validator**: Validação e estruturação de dados com pydanticAI.
4. **LLM Interface**: Integração com modelos OpenAI (gpt-4.1-nano agent).
5. **Extensibility Layer**: Pontos de extensão para futuras integrações (langgraphs, MCP, etc).

### Estrutura de Diretórios
```
src/
  academic_agent/
    core/
    workflows/
    validation/
    llm/
    extensions/
  tests/
  docs/
  examples/
  scripts/
```

## Tecnologias e Ferramentas

### Linguagem Principal
- **Python 3.10+**

### Bibliotecas Core
- **pydanticAI**: Validação e estruturação de dados inteligentes
- **openai**: Integração com modelos GPT-4.1-nano agent
- **pytest**: Testes automatizados
- **black**: Formatação de código
- **mypy**: Checagem de tipos

### Futuro / Planejado
- **langgraphs**: Workflows avançados de IA
- **MCP server**: Integração com protocolos abertos

## Considerações Técnicas

### Performance
- Processamento assíncrono para tarefas longas
- Modularidade para fácil extensão

### Segurança
- Validação rigorosa de entrada (pydanticAI)
- Limitação de uso de APIs externas

### Escalabilidade
- Arquitetura modular
- Suporte a múltiplos workflows simultâneos

## Fases de Desenvolvimento

### Fase 1: Foundation (Semana 1)
- Setup inicial do projeto
- Implementação do agente core e integração básica com OpenAI
- Testes unitários básicos

### Fase 2: Workflows Acadêmicos (Semanas 2-3)
- Implementação de workflows para redação, revisão e formatação
- Validação de dados com pydanticAI
- Testes de integração

### Fase 3: Extensões e Ferramentas (Semanas 4-5)
- Ferramentas para sumarização, explicação e tradução
- Pontos de extensão para integrações futuras
- Documentação e exemplos práticos

### Fase 4: Preparação para Produção (Semanas 6-7)
- Otimizações, logging e monitoramento
- Empacotamento e distribuição
- Planejamento para integração com langgraphs/MCP

## Critérios de Sucesso

### Técnicos
- Cobertura de testes > 90%
- Performance adequada para uso acadêmico
- Documentação completa

### Funcionais
- Workflows acadêmicos funcionando conforme especificado
- Facilidade de extensão e configuração
- Feedback positivo de usuários acadêmicos

## Riscos e Mitigações

### Riscos Técnicos
- **Mudança rápida em APIs de IA**: Monitorar releases e manter flexibilidade
- **Limitações de uso de modelos externos**: Planejar fallback e quotas

### Riscos de Projeto
- **Escopo excessivo**: Foco em MVP acadêmico
- **Adoção de novas tecnologias**: Prototipar antes de integrar

## Próximos Passos

1. Revisar e aprovar este plano
2. Configurar ambiente de desenvolvimento
3. Implementar estrutura básica do agente
4. Integrar OpenAI e pydanticAI
5. Planejar integrações futuras (langgraphs, MCP)

## Recursos Adicionais

- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Exemplos de implementação](https://github.com/modelcontextprotocol/servers)
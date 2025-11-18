#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Geração de Documentação Técnica Profissional
Projeto: RPA - Consulta Automatizada de Países
Autores: Felipe Viana, Ryan Rodrigues
Instituição: Faculdade Impacta de Tecnologia
Disciplina: Robotic Process Automation
Ano: 2025
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from datetime import datetime
from PIL import Image as PILImage
import sys

class TechnicalDocumentationGenerator:
    """Gerador de documentação técnica profissional para sistemas RPA"""
    
    def __init__(self):
        # Metadados do documento
        self.document_title = "Sistema RPA - Consulta Automatizada de Países"
        self.document_subtitle = "Documentação Técnica e Pipeline de Execução"
        self.authors = "Felipe Viana, Ryan Rodrigues"
        self.institution = "Faculdade Impacta de Tecnologia"
        self.department = "Departamento de Tecnologia da Informação"
        self.course = "Robotic Process Automation (RPA)"
        self.academic_year = "2025"
        self.version = "1.0"
        self.creation_date = datetime.now().strftime("%d de %B de %Y")
        
        # Configuração de arquivos
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.images_path = os.path.join(self.base_path, "images")
        self.output_file = os.path.join(os.path.dirname(__file__), "Documentacao_Tecnica_RPA_Paises.pdf")
        
        # Configurar estilos tipográficos
        self.styles = getSampleStyleSheet()
        self._configure_document_styles()
        
    def _configure_document_styles(self):
        """Configurar estilos tipográficos profissionais para o documento"""
        
        # Paleta de cores corporativa
        primary_blue = colors.HexColor('#1a365d')
        secondary_blue = colors.HexColor('#2d3748') 
        accent_blue = colors.HexColor('#3182ce')
        light_gray = colors.HexColor('#f7fafc')
        medium_gray = colors.HexColor('#e2e8f0')
        
        # Verificar se estilos já existem antes de adicionar
        style_names = [style.name for style in self.styles.byName.values()]
        
        # Estilo para título principal
        if 'DocumentTitle' not in style_names:
            self.styles.add(ParagraphStyle(
                name='DocumentTitle',
                parent=self.styles['Title'],
                fontSize=26,
                spaceAfter=24,
                spaceBefore=12,
                textColor=primary_blue,
                alignment=TA_CENTER,
                fontName='Helvetica-Bold',
                leading=30
            ))
        
        # Estilo para subtítulo
        if 'DocumentSubtitle' not in style_names:
            self.styles.add(ParagraphStyle(
                name='DocumentSubtitle',
                parent=self.styles['Normal'],
                fontSize=18,
                spaceAfter=36,
                spaceBefore=12,
                textColor=secondary_blue,
                alignment=TA_CENTER,
                fontName='Helvetica',
                leading=22
            ))
        
        # Estilo para cabeçalhos principais
        if 'ChapterHeading' not in style_names:
            self.styles.add(ParagraphStyle(
                name='ChapterHeading',
                parent=self.styles['Heading1'],
                fontSize=20,
                spaceAfter=18,
                spaceBefore=24,
                textColor=primary_blue,
                fontName='Helvetica-Bold',
                leading=24
            ))
        
        # Estilo para seções
        if 'SectionHeading' not in style_names:
            self.styles.add(ParagraphStyle(
                name='SectionHeading',
                parent=self.styles['Heading2'],
                fontSize=16,
                spaceAfter=14,
                spaceBefore=20,
                textColor=accent_blue,
                fontName='Helvetica-Bold',
                leading=20
            ))
        
        # Estilo para subseções
        if 'SubsectionHeading' not in style_names:
            self.styles.add(ParagraphStyle(
                name='SubsectionHeading',
                parent=self.styles['Heading3'],
                fontSize=14,
                spaceAfter=12,
                spaceBefore=16,
                textColor=secondary_blue,
                fontName='Helvetica-Bold',
                leading=18
            ))
        
        # Estilo para texto normal
        if 'BodyText' not in style_names:
            self.styles.add(ParagraphStyle(
                name='BodyText',
                parent=self.styles['Normal'],
                fontSize=11,
                spaceAfter=12,
                spaceBefore=0,
                alignment=TA_JUSTIFY,
                fontName='Helvetica',
                leading=14,
                firstLineIndent=0
            ))
        
        # Estilo para listas
        if 'BulletText' not in style_names:
            self.styles.add(ParagraphStyle(
                name='BulletText',
                parent=self.styles['Normal'],
                fontSize=11,
                spaceAfter=6,
                spaceBefore=0,
                leftIndent=20,
                bulletIndent=8,
                fontName='Helvetica',
                leading=14
            ))
        
        # Estilo para código
        if 'CodeBlock' not in style_names:
            self.styles.add(ParagraphStyle(
                name='CodeBlock',
                parent=self.styles['Normal'],
                fontSize=10,
                fontName='Courier-Bold',
                backColor=light_gray,
                borderColor=medium_gray,
                borderWidth=1,
                borderPadding=12,
                spaceAfter=12,
                spaceBefore=12,
                leftIndent=12,
                rightIndent=12
            ))
        
        # Estilo para citações/observações
        if 'NoteText' not in style_names:
            self.styles.add(ParagraphStyle(
                name='NoteText',
                parent=self.styles['Normal'],
                fontSize=10,
                fontName='Helvetica-Oblique',
                textColor=secondary_blue,
                spaceAfter=12,
                spaceBefore=6,
                leftIndent=16,
                rightIndent=16,
                leading=13
            ))

    def _optimize_image_dimensions(self, image_path, max_width=15*cm, max_height=10*cm):
        """Otimizar dimensões da imagem mantendo proporção"""
        try:
            with PILImage.open(image_path) as pil_image:
                original_width, original_height = pil_image.size
                
            aspect_ratio = original_width / original_height
            
            if original_width > original_height:
                final_width = min(max_width, max_width)
                final_height = final_width / aspect_ratio
                if final_height > max_height:
                    final_height = max_height
                    final_width = final_height * aspect_ratio
            else:
                final_height = min(max_height, max_height)
                final_width = final_height * aspect_ratio
                if final_width > max_width:
                    final_width = max_width
                    final_height = final_width / aspect_ratio
                    
            return final_width, final_height
        except Exception as error:
            print(f"Erro no processamento da imagem {image_path}: {error}")
            return 12*cm, 8*cm

    def _create_document_header(self, story):
        """Criar cabeçalho do documento"""
        
        story.append(Spacer(1, 1.5*inch))
        story.append(Paragraph(self.document_title, self.styles['DocumentTitle']))
        story.append(Paragraph(self.document_subtitle, self.styles['DocumentSubtitle']))
        
        story.append(Spacer(1, 0.8*inch))
        
        # Informações acadêmicas em tabela
        academic_info = [
            ["Instituição:", self.institution],
            ["Departamento:", self.department],
            ["Disciplina:", self.course],
            ["Ano Letivo:", self.academic_year],
            ["Versão:", self.version],
            ["Data de Criação:", self.creation_date]
        ]
        
        # Informações dos autores
        author_info = [
            ["Autores:", self.authors],
            ["Tipo de Documento:", "Documentação Técnica"],
            ["Tecnologias:", "Python 3.11, SQLite, REST API"],
            ["Categoria:", "Robotic Process Automation"]
        ]
        
        # Tabela de informações acadêmicas
        academic_table = Table(academic_info, colWidths=[4.5*cm, 9.5*cm])
        academic_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#1a365d')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8)
        ]))
        
        story.append(academic_table)
        story.append(Spacer(1, 0.5*inch))
        
        # Tabela de informações dos autores
        author_table = Table(author_info, colWidths=[4.5*cm, 9.5*cm])
        author_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#1a365d')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8)
        ]))
        
        story.append(author_table)
        story.append(Spacer(1, 0.8*inch))
        
        # Resumo executivo
        story.append(Paragraph("Resumo Executivo", self.styles['ChapterHeading']))
        executive_summary = """
        Este documento apresenta a documentação técnica completa do sistema de Robotic Process Automation (RPA) 
        desenvolvido para automatização de consulta e armazenamento de informações de países. O sistema integra 
        a API REST Countries com processamento de dados em Python e persistência em banco SQLite, oferecendo 
        uma solução robusta para coleta e organização automatizada de dados geográficos.
        
        A documentação inclui análise detalhada de cada componente do sistema, pipeline de execução visual, 
        especificações técnicas e diagramas de arquitetura, proporcionando uma visão abrangente do funcionamento 
        do sistema para fins educacionais, manutenção e evolução futura.
        """
        story.append(Paragraph(executive_summary, self.styles['BodyText']))
        
        story.append(PageBreak())

    def _create_system_overview(self, story):
        """Criar visão geral do sistema"""
        
        story.append(Paragraph("1. Visão Geral do Sistema", self.styles['ChapterHeading']))
        
        # Objetivo
        story.append(Paragraph("1.1 Objetivo", self.styles['SectionHeading']))
        objective_text = """
        O sistema RPA tem como objetivo automatizar o processo de consulta, processamento e armazenamento 
        de informações de países através da integração com a API REST Countries. O sistema elimina a 
        necessidade de busca manual de dados geográficos, implementando um fluxo automatizado que garante 
        consistência, precisão e eficiência na coleta de informações.
        """
        story.append(Paragraph(objective_text, self.styles['BodyText']))
        
        # Funcionalidades principais
        story.append(Paragraph("1.2 Funcionalidades Principais", self.styles['SectionHeading']))
        features = [
            "Coleta automatizada de nomes de países através de interface de linha de comando",
            "Busca inteligente com fallback utilizando múltiplos endpoints da API REST Countries",
            "Processamento e filtragem de dados JSON com correspondência exata",
            "Validação de duplicatas antes da inserção no banco de dados",
            "Armazenamento estruturado em banco SQLite com 14 campos de informação",
            "Suporte multilíngue para nomes de países em português e inglês",
            "Tratamento robusto de erros e exceções",
            "Feedback visual do status das operações"
        ]
        
        for feature in features:
            story.append(Paragraph(f"• {feature}", self.styles['BulletText']))
        
        story.append(Spacer(1, 0.3*inch))
        
        # Estrutura do projeto com imagem
        story.append(Paragraph("1.3 Estrutura do Projeto", self.styles['SectionHeading']))
        
        # Verificar se existe a imagem estrutura_projeto.png
        structure_image_path = os.path.join(self.images_path, "estrutura_projeto.png")
        if os.path.exists(structure_image_path):
            try:
                width, height = self._optimize_image_dimensions(structure_image_path, max_width=14*cm, max_height=8*cm)
                structure_img = Image(structure_image_path, width=width, height=height)
                story.append(Spacer(1, 0.2*inch))
                story.append(structure_img)
                story.append(Spacer(1, 0.3*inch))
            except Exception as e:
                print(f"Erro ao carregar imagem de estrutura: {e}")
        
        # Descrição textual da estrutura
        structure_description = """
        O projeto segue uma arquitetura modular organizada em camadas funcionais distintas. A estrutura 
        permite separação clara de responsabilidades, facilitando manutenção e evolução do sistema.
        """
        story.append(Paragraph(structure_description, self.styles['BodyText']))
        
        # Arquitetura do sistema
        story.append(Paragraph("1.4 Arquitetura do Sistema", self.styles['SectionHeading']))
        architecture_text = """
        O sistema adota uma arquitetura em camadas com separação clara de responsabilidades:
        """
        story.append(Paragraph(architecture_text, self.styles['BodyText']))
        
        # Componentes da arquitetura
        architecture_components = [
            "Camada de Apresentação: Interface de linha de comando para interação com usuário",
            "Camada de Negócio: Lógica de processamento, filtragem e validação de dados",
            "Camada de Integração: Comunicação com API externa REST Countries",
            "Camada de Persistência: Armazenamento e recuperação de dados em SQLite",
            "Camada de Modelo: Definição da estrutura de dados e esquema do banco"
        ]
        
        for component in architecture_components:
            story.append(Paragraph(f"• {component}", self.styles['BulletText']))
        
        story.append(PageBreak())

    def _create_technical_pipeline(self, story):
        """Criar documentação do pipeline técnico"""
        
        story.append(Paragraph("2. Pipeline de Execução Técnico", self.styles['ChapterHeading']))
        
        # Definição das etapas do pipeline
        pipeline_steps = [
            {
                "step": "Etapa 1",
                "title": "Inicialização do Sistema",
                "image": "codigo_core.jpg",
                "description": """
                O sistema é inicializado através do módulo principal main.py, que coordena a importação 
                e execução de todos os componentes necessários. Nesta etapa, são carregados os módulos 
                de conexão com banco de dados, coleta de input, processamento de dados e inserção.
                
                Componentes carregados:
                • models.paises: Estabelece conexão com banco SQLite e define estrutura da tabela
                • core.input: Responsável pela coleta de dados do usuário
                • core.filter: Implementa lógica de processamento e filtragem de dados da API
                • core.insert: Gerencia inserção de dados e controle de duplicatas
                
                A função main() atua como orquestrador central, coordenando o fluxo de execução 
                entre todos os módulos do sistema.
                """,
                "technical_notes": "Utiliza padrão de importação modular para separação de responsabilidades"
            },
            {
                "step": "Etapa 2", 
                "title": "Configuração do Banco de Dados",
                "image": "criar_banco_dados.jpg",
                "description": """
                O sistema configura automaticamente o ambiente de persistência criando o banco de dados 
                SQLite na pasta data/ caso não exista. A conexão é estabelecida e mantida durante toda 
                a execução para garantir integridade transacional.
                
                Configurações realizadas:
                • Criação automática do diretório data/ se não existir
                • Estabelecimento de conexão SQLite com o arquivo paises.db
                • Configuração de timeout e parâmetros de conexão
                • Preparação do cursor para execução de comandos SQL
                
                O SQLite é utilizado por ser um banco embarcado que não requer instalação ou 
                configuração de servidor, ideal para aplicações RPA de pequeno e médio porte.
                """,
                "technical_notes": "SQLite oferece ACID compliance e suporte completo a SQL padrão"
            },
            {
                "step": "Etapa 3",
                "title": "Definição do Esquema de Dados", 
                "image": "tabela_paises_db.jpg",
                "description": """
                A tabela 'paises' é criada seguindo um esquema normalizado com 14 campos que capturam 
                informações abrangentes sobre cada país. O esquema foi projetado para acomodar todos 
                os dados relevantes fornecidos pela API REST Countries.
                
                Estrutura da tabela:
                • Identificadores: id (chave primária), nome_comum, nome_oficial
                • Localização: capital, continente, regiao, subregiao
                • Demografia: populacao (INTEGER)
                • Geografia: area (REAL)
                • Economia: moeda_nome, moeda_simbolo
                • Cultura: idioma_principal
                • Metadados: fuso_horario, bandeira_url
                
                O esquema utiliza tipos de dados apropriados para cada campo, garantindo integridade 
                referencial e otimização de armazenamento.
                """,
                "technical_notes": "Esquema projetado para normalização e eficiência de consultas"
            },
            {
                "step": "Etapa 4",
                "title": "Coleta de Dados do Usuário",
                "image": "obter_paises_db.jpg", 
                "description": """
                O módulo de input implementa um loop controlado que solicita ao usuário o nome de 
                três países através de interface de linha de comando. O sistema padroniza todas 
                as entradas convertendo para lowercase para garantir consistência no processamento.
                
                Processo de coleta:
                • Loop iterativo com contador de 1 a 3
                • Prompt personalizado indicando a posição do país
                • Conversão automática para lowercase
                • Armazenamento em lista para processamento posterior
                • Retorno da lista completa ao módulo principal
                
                A interface foi projetada para ser intuitiva e fornecer feedback claro ao usuário 
                sobre o progresso da coleta de dados.
                """,
                "technical_notes": "Interface de linha de comando com validação básica de entrada"
            },
            {
                "step": "Etapa 5",
                "title": "Processamento da Lista de Países",
                "image": "output_paises.jpg",
                "description": """
                Após a coleta, o sistema processa a lista de países retornada, preparando-a para 
                as operações subsequentes de busca na API. Cada país na lista será processado 
                individualmente através de um loop iterativo.
                
                Operações realizadas:
                • Validação da lista retornada pela função obter_paises()
                • Preparação para iteração sobre cada elemento
                • Inicialização do contexto de processamento para cada país
                • Configuração de variáveis de controle para o loop principal
                
                Esta etapa marca a transição da fase de coleta para a fase de processamento 
                de dados do sistema.
                """,
                "technical_notes": "Implementa padrão iterator para processamento sequencial"
            },
            {
                "step": "Etapa 6",
                "title": "Invocação do Módulo de Filtragem",
                "image": "filtrar_dados.jpg",
                "description": """
                Para cada país na lista, o sistema invoca o módulo de filtragem que coordena 
                a busca na API e o processamento dos dados retornados. Esta etapa implementa 
                a lógica central de processamento do sistema.
                
                Responsabilidades do módulo:
                • Coordenação da busca na API através do módulo api.buscar_pais()
                • Implementação de algoritmo de correspondência exata
                • Estruturação dos dados em formato adequado para persistência
                • Tratamento de casos onde múltiplos países são retornados
                • Retorno de dicionário estruturado ou None em caso de erro
                
                O módulo atua como intermediário entre a API externa e a camada de persistência.
                """,
                "technical_notes": "Implementa padrão de coordenação entre camadas de sistema"
            },
            {
                "step": "Etapa 7",
                "title": "Requisição à API REST Countries",
                "image": "buscar_pais.jpg",
                "description": """
                O módulo de API implementa estratégia de busca com fallback utilizando dois endpoints 
                da REST Countries API. Esta abordagem maximiza a taxa de sucesso na busca por países.
                
                Estratégia de busca:
                1. Tentativa primária: endpoint /translation/{país}
                   - Aceita nomes em múltiplos idiomas, incluindo português
                   - Permite busca por "França", "México", "Japão" diretamente
                   
                2. Tentativa secundária: endpoint /name/{país}
                   - Utilizado como fallback quando a primeira tentativa falha
                   - Busca por nomes em inglês e variações oficiais
                
                O sistema retorna os dados JSON completos ou None caso ambas as tentativas falhem.
                """,
                "technical_notes": "Implementa padrão de fallback para robustez na integração"
            },
            {
                "step": "Etapa 8",
                "title": "Processamento da Resposta JSON",
                "image": "json_paises.jpg",
                "description": """
                A API REST Countries retorna um array JSON contendo todos os países que correspondem 
                aos critérios de busca. Em muitos casos, múltiplos países podem ser retornados para 
                uma única busca, exigindo processamento adicional para identificar o país correto.
                
                Estrutura da resposta:
                • Array de objetos JSON, cada um representando um país
                • Cada objeto contém campos como name, capital, population, area, etc.
                • Campo translations contém nomes do país em diversos idiomas
                • Campos currencies e languages são objetos aninhados
                
                O processamento desta resposta requer algoritmo de correspondência para selecionar 
                o país correto quando múltiplas opções são retornadas.
                """,
                "technical_notes": "JSON estruturado seguindo padrão REST API com objetos aninhados"
            },
            {
                "step": "Etapa 9",
                "title": "Algoritmo de Correspondência Exata",
                "image": None,
                "description": """
                O sistema implementa algoritmo sofisticado de correspondência que compara o termo 
                buscado com múltiplos campos de cada país retornado pela API, garantindo seleção 
                precisa do país desejado.
                
                Critérios de correspondência:
                • Comparação com name.common (nome comum em inglês)
                • Comparação com name.official (nome oficial completo)
                • Comparação com translations.por.common (nome em português, se disponível)
                • Todas as comparações são case-insensitive
                • Correspondência exata interrompe o loop (break)
                
                Algoritmo:
                for país in dados_json:
                    if termo_buscado == nome_comum OR nome_oficial OR nome_português:
                        selecionar_país(país)
                        break
                        
                Caso nenhuma correspondência exata seja encontrada, o sistema utiliza o primeiro 
                país da lista como fallback.
                """,
                "technical_notes": "Algoritmo O(n) com terminação antecipada para otimização"
            },
            {
                "step": "Etapa 10",
                "title": "Estruturação de Dados para Persistência",
                "image": "insert_paises.jpg",
                "description": """
                Após identificar o país correto, o sistema extrai e estrutura os dados necessários 
                em um dicionário Python que mapeia diretamente para os campos da tabela do banco 
                de dados.
                
                Processo de estruturação:
                • Extração de 13 campos específicos do objeto JSON
                • Tratamento de campos opcionais e arrays (capital, currencies, languages)
                • Conversão de tipos de dados quando necessário
                • Tratamento de valores nulos ou ausentes
                • Criação de dicionário com chaves correspondentes às colunas da tabela
                
                O dicionário resultante é passado para a camada de persistência junto com 
                o nome original buscado pelo usuário.
                """,
                "technical_notes": "Mapeamento objeto-relacional manual para controle de dados"
            },
            {
                "step": "Etapa 11",
                "title": "Validação de Duplicatas e Inserção",
                "image": "paises_inseridos.jpg",
                "description": """
                O módulo de inserção implementa validação de duplicatas antes de persistir dados 
                no banco. Esta verificação previne inconsistências e garante integridade referencial.
                
                Processo de validação:
                • Execução de consulta SELECT para verificar existência do país
                • Comparação baseada no campo nome_comum
                • Retorno de False caso o país já exista
                • Execução de INSERT caso o país seja novo
                • Commit da transação e retorno de True em caso de sucesso
                
                Feedback ao usuário:
                • Mensagens de sucesso para países inseridos
                • Avisos para países já existentes
                • Mensagens de erro para falhas na API
                
                O sistema mantém log detalhado de todas as operações realizadas.
                """,
                "technical_notes": "Controle transacional com rollback automático em caso de erro"
            },
            {
                "step": "Etapa 12",
                "title": "Finalização e Limpeza de Recursos",
                "image": "tabela_sqlite.jpg",
                "description": """
                Após processar todos os países, o sistema executa rotinas de finalização que 
                incluem fechamento de conexões e liberação de recursos do sistema.
                
                Operações de finalização:
                • Fechamento da conexão com banco de dados através de db.close()
                • Liberação de cursores e handlers de conexão
                • Limpeza de variáveis temporárias
                • Confirmação de todas as transações pendentes
                
                Estado final:
                • Banco de dados atualizado com novos países
                • Todas as conexões adequadamente fechadas
                • Sistema pronto para nova execução
                • Log completo de operações disponível
                
                A tabela final contém todos os países processados com informações completas 
                extraídas da API REST Countries.
                """,
                "technical_notes": "Implementa padrão de cleanup para gerenciamento de recursos"
            }
        ]
        
        # Processar cada etapa do pipeline
        for i, step in enumerate(pipeline_steps):
            # Cabeçalho da etapa
            step_header = f"2.{i+1} {step['step']}: {step['title']}"
            story.append(Paragraph(step_header, self.styles['SectionHeading']))
            
            # Inserir imagem se disponível
            if step['image']:
                image_path = os.path.join(self.images_path, step['image'])
                if os.path.exists(image_path):
                    try:
                        width, height = self._optimize_image_dimensions(image_path, max_width=14*cm, max_height=8*cm)
                        img = Image(image_path, width=width, height=height)
                        story.append(Spacer(1, 0.2*inch))
                        story.append(img)
                        story.append(Spacer(1, 0.25*inch))
                    except Exception as e:
                        story.append(Paragraph(f"[Imagem indisponível: {step['image']}]", self.styles['NoteText']))
                        print(f"Erro ao processar imagem {step['image']}: {e}")
            
            # Descrição técnica
            story.append(Paragraph(step['description'], self.styles['BodyText']))
            
            # Nota técnica se disponível
            if 'technical_notes' in step:
                note_text = f"Nota Técnica: {step['technical_notes']}"
                story.append(Paragraph(note_text, self.styles['NoteText']))
            
            story.append(Spacer(1, 0.3*inch))
            
            # Page break a cada 3 etapas para melhor organização
            if (i + 1) % 3 == 0 and i < len(pipeline_steps) - 1:
                story.append(PageBreak())

    def _create_technical_specifications(self, story):
        """Criar especificações técnicas detalhadas"""
        
        story.append(PageBreak())
        story.append(Paragraph("3. Especificações Técnicas", self.styles['ChapterHeading']))
        
        # Stack tecnológico
        story.append(Paragraph("3.1 Stack Tecnológico", self.styles['SectionHeading']))
        
        tech_stack_data = [
            ["Componente", "Tecnologia", "Versão", "Finalidade", "Licença"],
            ["Runtime", "Python", "3.11+", "Linguagem de programação principal", "PSF"],
            ["Banco de Dados", "SQLite", "3.x", "Persistência de dados embarcada", "Public Domain"],
            ["API Externa", "REST Countries", "v3.1", "Fonte de dados geográficos", "Mozilla Public License"],
            ["Cliente HTTP", "Requests", "2.x", "Comunicação com APIs REST", "Apache 2.0"],
            ["Processamento PDF", "ReportLab", "4.x", "Geração de documentação", "BSD"],
            ["Manipulação de Imagens", "Pillow", "10.x", "Processamento de imagens", "HPND"]
        ]
        
        tech_table = Table(tech_stack_data, colWidths=[2.5*cm, 2.8*cm, 1.5*cm, 4.5*cm, 2.7*cm])
        tech_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a365d')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6)
        ]))
        
        story.append(tech_table)
        story.append(Spacer(1, 0.4*inch))
        
        # Arquitetura de dados
        story.append(Paragraph("3.2 Arquitetura de Dados", self.styles['SectionHeading']))
        data_architecture_text = """
        O sistema utiliza arquitetura de dados simplificada com foco em eficiência e manutenibilidade. 
        A escolha do SQLite como banco de dados embarcado elimina complexidades de configuração e 
        oferece performance adequada para o volume de dados esperado.
        """
        story.append(Paragraph(data_architecture_text, self.styles['BodyText']))
        
        # Esquema do banco
        story.append(Paragraph("3.2.1 Esquema do Banco de Dados", self.styles['SubsectionHeading']))
        
        database_schema_data = [
            ["Campo", "Tipo", "Nulo", "Descrição", "Origem API"],
            ["id", "INTEGER PRIMARY KEY", "Não", "Identificador único auto-incremento", "N/A"],
            ["nome_comum", "TEXT", "Não", "Nome comum do país", "name.common"],
            ["nome_oficial", "TEXT", "Sim", "Nome oficial completo", "name.official"],
            ["capital", "TEXT", "Sim", "Cidade capital", "capital[0]"],
            ["continente", "TEXT", "Sim", "Continente", "continents[0]"],
            ["regiao", "TEXT", "Sim", "Região geográfica", "region"],
            ["subregiao", "TEXT", "Sim", "Sub-região específica", "subregion"],
            ["populacao", "INTEGER", "Sim", "População total", "population"],
            ["area", "REAL", "Sim", "Área territorial em km²", "area"],
            ["moeda_nome", "TEXT", "Sim", "Nome da moeda oficial", "currencies.*.name"],
            ["moeda_simbolo", "TEXT", "Sim", "Símbolo da moeda", "currencies.*.symbol"],
            ["idioma_principal", "TEXT", "Sim", "Idioma principal", "languages.*[0]"],
            ["fuso_horario", "TEXT", "Sim", "Fuso horário principal", "timezones[0]"],
            ["bandeira_url", "TEXT", "Sim", "URL da imagem da bandeira", "flags.png"]
        ]
        
        schema_table = Table(database_schema_data, colWidths=[2.8*cm, 3*cm, 1.2*cm, 3.5*cm, 3.5*cm])
        schema_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2d3748')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 8),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 7),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4)
        ]))
        
        story.append(schema_table)
        story.append(Spacer(1, 0.4*inch))
        
        # Especificações da API
        story.append(Paragraph("3.3 Integração com API REST Countries", self.styles['SectionHeading']))
        api_description = """
        A integração com a API REST Countries v3.1 fornece dados geográficos abrangentes e atualizados. 
        A API oferece múltiplos endpoints que permitem diferentes estratégias de busca.
        """
        story.append(Paragraph(api_description, self.styles['BodyText']))
        
        api_endpoints_data = [
            ["Endpoint", "Método", "Parâmetros", "Descrição"],
            ["/v3.1/translation/{termo}", "GET", "termo: string", "Busca por traduções em múltiplos idiomas"],
            ["/v3.1/name/{nome}", "GET", "nome: string", "Busca por nome oficial ou comum"],
            ["/v3.1/all", "GET", "nenhum", "Retorna todos os países (não utilizado)"]
        ]
        
        api_table = Table(api_endpoints_data, colWidths=[4.5*cm, 2*cm, 3*cm, 4.5*cm])
        api_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3182ce')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8)
        ]))
        
        story.append(api_table)
        
        # Performance e limitações
        story.append(Spacer(1, 0.4*inch))
        story.append(Paragraph("3.4 Performance e Limitações", self.styles['SectionHeading']))
        performance_text = """
        O sistema foi projetado para processar até 3 países por execução, mantendo simplicidade 
        e eficiência. A API REST Countries não possui limites de rate limiting documentados, 
        mas o sistema implementa apenas requisições sequenciais para evitar sobrecarga.
        
        Limitações identificadas:
        • Processamento limitado a 3 países por execução
        • Dependência de conectividade com internet para acesso à API
        • Busca por apelidos não oficiais não suportada (ex: "EUA", "Inglaterra")
        • Sem cache local dos dados da API
        • Interface limitada a linha de comando
        """
        story.append(Paragraph(performance_text, self.styles['BodyText']))

    def _create_appendices(self, story):
        """Criar apêndices com informações complementares"""
        
        story.append(PageBreak())
        story.append(Paragraph("4. Apêndices", self.styles['ChapterHeading']))
        
        # Código fonte principal
        story.append(Paragraph("4.1 Estrutura de Código", self.styles['SectionHeading']))
        code_structure_text = """
        O sistema segue princípios de programação modular com separação clara de responsabilidades. 
        Cada módulo tem função específica e interfaces bem definidas.
        """
        story.append(Paragraph(code_structure_text, self.styles['BodyText']))
        
        # Dependências
        story.append(Paragraph("4.2 Gerenciamento de Dependências", self.styles['SectionHeading']))
        dependencies_text = """
        O arquivo requirements.txt centraliza todas as dependências do projeto:
        """
        story.append(Paragraph(dependencies_text, self.styles['BodyText']))
        
        requirements_code = """requests==2.31.0
reportlab==4.0.4
Pillow==10.0.0"""
        story.append(Paragraph(requirements_code, self.styles['CodeBlock']))
        
        # Instalação e configuração
        story.append(Paragraph("4.3 Procedimentos de Instalação", self.styles['SectionHeading']))
        installation_steps = [
            "Clonar o repositório do projeto",
            "Navegar para o diretório do projeto",
            "Criar ambiente virtual Python (recomendado)",
            "Instalar dependências: pip install -r requirements.txt",
            "Executar o sistema: python main.py",
            "Verificar criação do diretório data/ e arquivo paises.db"
        ]
        
        for step in installation_steps:
            story.append(Paragraph(f"• {step}", self.styles['BulletText']))
        
        story.append(Spacer(1, 0.3*inch))
        
        # Troubleshooting
        story.append(Paragraph("4.4 Solução de Problemas", self.styles['SectionHeading']))
        troubleshooting_text = """
        Problemas comuns e soluções:
        
        Erro de conectividade com API:
        • Verificar conexão com internet
        • Validar disponibilidade da API REST Countries
        • Confirmar firewall não está bloqueando requisições HTTP
        
        Erro de permissão no banco de dados:
        • Verificar permissões de escrita no diretório do projeto
        • Confirmar que o diretório data/ pode ser criado
        • Validar que não há outros processos usando o arquivo paises.db
        
        País não encontrado:
        • Verificar ortografia do nome do país
        • Tentar variações (português/inglês)
        • Usar nomes oficiais completos quando possível
        """
        story.append(Paragraph(troubleshooting_text, self.styles['BodyText']))
        
        # Informações sobre autores
        story.append(Paragraph("4.5 Informações dos Autores", self.styles['SectionHeading']))
        authors_info = f"""
        Este projeto foi desenvolvido como trabalho acadêmico para a disciplina de Robotic Process 
        Automation da {self.institution}.
        
        Autores: {self.authors}
        Orientação: Corpo docente da disciplina RPA
        Período: {self.academic_year}
        
        Para questões técnicas ou sugestões de melhoria, entrar em contato através dos canais 
        acadêmicos oficiais da instituição.
        """
        story.append(Paragraph(authors_info, self.styles['BodyText']))

    def generate_documentation(self):
        """Método principal para geração da documentação"""
        try:
            # Verificar existência do diretório de imagens
            if not os.path.exists(self.images_path):
                raise FileNotFoundError(f"Diretório de imagens não encontrado: {self.images_path}")
            
            # Configurar documento PDF
            pdf_document = SimpleDocTemplate(
                self.output_file,
                pagesize=A4,
                rightMargin=2.5*cm,
                leftMargin=2.5*cm,
                topMargin=2*cm,
                bottomMargin=2*cm,
                title=self.document_title,
                author=self.authors
            )
            
            # Inicializar conteúdo do documento
            document_content = []
            
            # Construir seções do documento
            print("Criando cabeçalho do documento...")
            self._create_document_header(document_content)
            
            print("Gerando visão geral do sistema...")
            self._create_system_overview(document_content)
            
            print("Documentando pipeline técnico...")
            self._create_technical_pipeline(document_content)
            
            print("Compilando especificações técnicas...")
            self._create_technical_specifications(document_content)
            
            print("Adicionando apêndices...")
            self._create_appendices(document_content)
            
            # Gerar arquivo PDF
            print("Compilando documento PDF...")
            pdf_document.build(document_content)
            
            print(f"Documentação gerada com sucesso: {self.output_file}")
            return True
            
        except Exception as error:
            print(f"Erro na geração da documentação: {error}")
            return False

def main():
    """Função principal de execução"""
    print("Sistema de Geração de Documentação Técnica")
    print("Projeto: RPA - Consulta Automatizada de Países")
    print("=" * 60)
    
    try:
        documentation_generator = TechnicalDocumentationGenerator()
        success = documentation_generator.generate_documentation()
        
        if success:
            print(f"\nDocumentação técnica gerada com sucesso!")
            print(f"Arquivo: {documentation_generator.output_file}")
            print(f"Tamanho estimado: arquivo PDF completo")
            return 0
        else:
            print("\nFalha na geração da documentação técnica")
            return 1
            
    except Exception as error:
        print(f"\nErro crítico no sistema: {error}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

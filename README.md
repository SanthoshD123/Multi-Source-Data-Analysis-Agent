# 🤖 Multi-Source Data Analysis Agent

A powerful AI-driven data analysis tool that can read from multiple sources, analyze patterns, and generate intelligent insights with beautiful visualizations.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-green.svg)

## 🎯 Project Overview

This project demonstrates advanced agentic AI capabilities by combining multiple specialized agents:
- **Data Reader Agent**: Handles various data sources (CSV, Excel, APIs, databases)
- **Analyzer Agent**: Performs statistical analysis and generates AI-powered insights
- **Visualizer Agent**: Creates intelligent, interactive visualizations

Perfect for showcasing AI engineering skills to top tech companies!

## ✨ Features

### 🔍 **Multi-Source Data Integration**
- CSV and Excel file support
- REST API integration
- SQLite database connectivity
- Real-time data processing

### 🤖 **AI-Powered Analysis**
- Automated pattern detection
- Natural language insights
- Correlation analysis
- Trend identification
- Interactive AI chat interface

### 📊 **Smart Visualizations**
- Auto-generated charts based on data types
- Custom chart builder
- Interactive dashboards
- Multiple chart types (bar, line, scatter, heatmaps)

### 🚀 **User Experience**
- Clean, intuitive Streamlit interface
- Real-time processing
- Error handling and validation
- Responsive design

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/multi-source-data-agent.git
cd multi-source-data-agent
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Get OpenAI API Key**
- Visit [OpenAI Platform](https://platform.openai.com)
- Create account and generate API key
- Keep the key ready (starts with `sk-...`)

## 🚀 Usage

### Running the Application

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Interface

1. **Enter API Key**: Add your OpenAI API key in the sidebar
2. **Upload Data**: Use the "Data Input" tab to upload CSV/Excel files or try sample data
3. **Analyze**: View automatic analysis in the "Analysis" tab
4. **Visualize**: Generate charts in the "Visualization" tab
5. **Chat with AI**: Ask questions about your data in the "AI Chat" tab

### Sample Data

The project includes `sample_data.csv` with business metrics including:
- Daily sales and profit data
- Regional performance
- Category analysis
- Customer satisfaction scores
- Employee and marketing data

## 📁 Project Structure

```
my_data_agent/
├── main.py                 # Main Streamlit application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── agents/               # AI agent modules
│   ├── __init__.py
│   ├── data_reader.py    # Data ingestion agent
│   ├── analyzer.py       # Analysis and AI insights agent
│   └── visualizer.py     # Visualization agent
├── data/                 # Data files
│   └── sample_data.csv   # Sample dataset
└── temp/                 # Temporary files
```

## 🧠 Agent Architecture

### Data Reader Agent
```python
- read_csv(): Process CSV files
- read_excel(): Handle Excel files  
- read_api(): Fetch data from REST APIs
- read_database(): Query SQLite databases
- get_data_info(): Extract data metadata
```

### Analyzer Agent
```python
- basic_statistics(): Generate statistical summaries
- ai_insights(): Create AI-powered insights
- find_trends(): Detect patterns and correlations
```

### Visualizer Agent
```python
- auto_visualize(): Generate charts automatically
- create_custom_chart(): Build specific visualizations
- create_dashboard(): Compose multi-chart dashboards
```

## 🔧 Technical Details

### Tech Stack
- **Frontend**: Streamlit (Python web framework)
- **AI/ML**: OpenAI GPT-3.5, LangChain
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Plotly Express
- **Database**: SQLAlchemy, SQLite
- **APIs**: Requests library

### Key Libraries
```python
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.15.0
openai>=1.0.0
langchain>=0.1.0
sqlalchemy>=2.0.0
requests>=2.31.0
openpyxl>=3.1.0
```

## 🎯 Use Cases

### Business Analytics
- Sales performance analysis
- Customer behavior insights
- Market trend identification
- Financial reporting automation

### Data Science Projects
- Exploratory data analysis
- Pattern recognition
- Correlation studies
- Automated reporting

### Enterprise Solutions
- Multi-source data integration
- Real-time analytics dashboards
- AI-powered business intelligence
- Data quality assessment

## 🚦 API Integration Examples

### Weather Data
```python
weather_data = reader_agent.read_api(
    "https://api.openweathermap.org/data/2.5/weather",
    params={"q": "London", "appid": "your_key"}
)
```

### Financial Data
```python
stock_data = reader_agent.read_api(
    "https://api.example.com/stocks",
    params={"symbol": "AAPL", "interval": "1d"}
)
```

## 📊 Sample Analysis Output

The system can generate insights like:
- "Sales show strong positive correlation with marketing spend (r=0.85)"
- "West region consistently outperforms other regions by 23%"
- "Customer satisfaction scores are highest for Electronics category"
- "Seasonal trends indicate Q4 peak performance"

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Future Enhancements

### Planned Features
- [ ] MySQL/PostgreSQL support
- [ ] Real-time data streaming
- [ ] Machine learning model integration
- [ ] Advanced NLP for data queries
- [ ] Multi-user collaboration
- [ ] Cloud deployment templates
- [ ] Custom agent creation interface

### Advanced Capabilities
- [ ] Automated data cleaning
- [ ] Predictive analytics
- [ ] Anomaly detection
- [ ] A/B testing analysis
- [ ] Time series forecasting

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- **AI Agent Architecture**: Multi-agent system design
- **Data Engineering**: ETL processes and data integration
- **Machine Learning**: Pattern recognition and analysis
- **Full-Stack Development**: End-to-end application development
- **API Integration**: RESTful services and third-party APIs
- **Data Visualization**: Interactive dashboard creation
- **Software Engineering**: Clean code, documentation, testing

## 🏢 Enterprise Readiness

### Scalability Features
- Modular agent architecture
- Configurable data sources
- Error handling and logging
- Performance optimization
- Memory-efficient processing

### Security Considerations
- API key management
- Input validation
- Error handling
- Data privacy compliance ready

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing GPT-3.5 API
- Streamlit team for the amazing framework
- Plotly for interactive visualizations
- The open-source community

## 🎯 Portfolio Impact

This project showcases:
- **AI Engineering Skills**: Multi-agent systems, LangChain integration
- **Data Science Expertise**: Statistical analysis, pattern recognition
- **Full-Stack Capabilities**: Python, web frameworks, APIs
- **Business Acumen**: Real-world application, enterprise features
- **Technical Leadership**: Architecture design, documentation

Perfect for landing roles at: Google, Microsoft, Amazon, Meta, Netflix, Uber, Airbnb, and other top tech companies!

---

⭐ **Star this repository if it helped you land your dream job!** ⭐

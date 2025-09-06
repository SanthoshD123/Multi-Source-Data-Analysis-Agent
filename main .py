import streamlit as st
import pandas as pd
from agents.data_reader import DataReaderAgent
from agents.analyzer import AnalyzerAgent
from agents.visualizer import VisualizerAgent
import os

# Configure the page
st.set_page_config(
    page_title="Multi-Source Data Analysis Agent",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame()
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False

def main():
    st.title("🤖 Multi-Source Data Analysis Agent")
    st.markdown("### Your AI-powered data analysis companion!")
    
    # Sidebar for API key
    with st.sidebar:
        st.header("🔐 Configuration")
        api_key = st.text_input("OpenAI API Key", type="password")
        if not api_key:
            st.warning("Please enter your OpenAI API key to use AI analysis features")
    
    # Initialize agents
    reader_agent = DataReaderAgent()
    if api_key:
        analyzer_agent = AnalyzerAgent(api_key)
    visualizer_agent = VisualizerAgent()
    
    # Main interface
    tab1, tab2, tab3, tab4 = st.tabs(["📁 Data Input", "🔍 Analysis", "📊 Visualization", "🤖 AI Chat"])
    
    with tab1:
        st.header("Data Input")
        
        # File upload section
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📁 Upload Files")
            uploaded_file = st.file_uploader(
                "Upload CSV or Excel file", 
                type=['csv', 'xlsx', 'xls']
            )
            
            if uploaded_file:
                if uploaded_file.name.endswith('.csv'):
                    data = reader_agent.read_csv(uploaded_file)
                else:
                    data = reader_agent.read_excel(uploaded_file)
                
                if not data.empty:
                    st.session_state.data = data
                    st.success(f"✅ Loaded {len(data)} rows and {len(data.columns)} columns")
                    st.dataframe(data.head())
        
        with col2:
            st.subheader("🌐 API Data")
            api_url = st.text_input("Enter API URL (optional)")
            if st.button("Fetch API Data") and api_url:
                data = reader_agent.read_api(api_url)
                if not data.empty:
                    st.session_state.data = data
                    st.success(f"✅ Loaded {len(data)} rows from API")
                    st.dataframe(data.head())
        
        # Sample data option
        if st.button("🎯 Use Sample Data"):
            # Create sample data
            sample_data = pd.DataFrame({
                'date': pd.date_range('2024-01-01', periods=100, freq='D'),
                'sales': [100 + i*2 + (i%7)*10 for i in range(100)],
                'category': ['A', 'B', 'C'] * 33 + ['A'],
                'region': ['North', 'South'] * 50
            })
            st.session_state.data = sample_data
            st.success("✅ Sample data loaded!")
            st.dataframe(sample_data.head())
    
    with tab2:
        st.header("Data Analysis")
        
        if st.session_state.data.empty:
            st.warning("Please upload data first!")
        else:
            data = st.session_state.data
            
            # Basic info
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Rows", len(data))
            with col2:
                st.metric("Total Columns", len(data.columns))
            with col3:
                st.metric("Missing Values", data.isnull().sum().sum())
            
            # Data info
            st.subheader("📋 Data Overview")
            data_info = reader_agent.get_data_info(data)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Column Information:**")
                info_df = pd.DataFrame({
                    'Column': data.columns,
                    'Type': [str(dtype) for dtype in data.dtypes],
                    'Missing': data.isnull().sum().values
                })
                st.dataframe(info_df)
            
            with col2:
                st.write("**Basic Statistics:**")
                if api_key:
                    basic_stats = analyzer_agent.basic_statistics(data)
                    if basic_stats.get('numeric_summary'):
                        st.write("Numeric columns summary:")
                        st.json(basic_stats['numeric_summary'])
                
                # Find trends
                if api_key:
                    trends = analyzer_agent.find_trends(data)
                    st.write("**Detected Patterns:**")
                    for trend in trends:
                        st.write(f"• {trend}")
    
    with tab3:
        st.header("Data Visualization")
        
        if st.session_state.data.empty:
            st.warning("Please upload data first!")
        else:
            data = st.session_state.data
            
            # Auto-generate charts
            st.subheader("🎨 Auto-Generated Charts")
            if st.button("Generate Automatic Charts"):
                charts = visualizer_agent.auto_visualize(data)
                
                for i, chart in enumerate(charts):
                    st.plotly_chart(chart, use_container_width=True)
            
            # Custom chart creation
            st.subheader("🛠️ Create Custom Chart")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                chart_type = st.selectbox("Chart Type", ['bar', 'line', 'scatter', 'histogram'])
            with col2:
                x_col = st.selectbox("X Column", data.columns)
            with col3:
                numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
                y_col = st.selectbox("Y Column (optional)", ['None'] + numeric_cols)
                y_col = None if y_col == 'None' else y_col
            
            if st.button("Create Chart"):
                custom_chart = visualizer_agent.create_custom_chart(data, chart_type, x_col, y_col)
                st.plotly_chart(custom_chart, use_container_width=True)
            
            # Dashboard
            if st.button("📊 Create Dashboard"):
                dashboard = visualizer_agent.create_dashboard(data)
                st.plotly_chart(dashboard, use_container_width=True)
    
    with tab4:
        st.header("AI Chat Analysis")
        
        if not api_key:
            st.warning("Please enter your OpenAI API key in the sidebar to use this feature")
        elif st.session_state.data.empty:
            st.warning("Please upload data first!")
        else:
            st.subheader("🤖 Ask AI About Your Data")
            
            user_question = st.text_input(
                "Ask a question about your data:",
                placeholder="What are the main trends in this data?"
            )
            
            if st.button("Ask AI") and user_question:
                with st.spinner("AI is analyzing your data..."):
                    data_info = reader_agent.get_data_info(st.session_state.data)
                    insights = analyzer_agent.ai_insights(data_info, user_question)
                    st.write("**AI Response:**")
                    st.write(insights)
            
            # Quick analysis buttons
            st.subheader("🚀 Quick Analysis")
            quick_questions = [
                "Summarize the key patterns in this data",
                "What are the most important insights?",
                "Are there any data quality issues?",
                "What recommendations do you have?"
            ]
            
            for question in quick_questions:
                if st.button(question):
                    with st.spinner("Analyzing..."):
                        data_info = reader_agent.get_data_info(st.session_state.data)
                        insights = analyzer_agent.ai_insights(data_info, question)
                        st.write(f"**{question}**")
                        st.write(insights)
    
    # Footer
    st.markdown("---")
    st.markdown("🚀 Built with Streamlit, OpenAI, and lots of ☕")

if __name__ == "__main__":
    main()

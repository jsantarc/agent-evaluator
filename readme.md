# Agent Evaluator

A minimal Gradio interface for testing and validating chatbot agents across different stages.

## 🎯 Purpose

This repository provides a lightweight framework for chatbot validation testing. Built with minimal code to focus on agent evaluation rather than complex infrastructure.

## 🚀 Features

- **Minimal Codebase**: Clean, simple implementation for quick setup and testing
- **Gradio Interface**: User-friendly chat interface for interactive agent evaluation
- **LangChain Integration**: Conversation memory and chain management
- **OpenAI Integration**: Tests agents powered by GPT models
- **Docker Support**: Containerized for consistent deployment

## 📋 Requirements

- Python 3.11+
- OpenAI API key
- Docker (for containerized deployment)

## 🛠️ Local Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd agent-evaluator
   ```

2. **Create `.env` file**
   ```bash
   echo "OPENAI_API_KEY=your-key-here" > .env
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the interface**
   - Open browser to `http://localhost:7860`

## 🐳 Docker Deployment

1. **Build the image**
   ```bash
   docker build -t agent-evaluator .
   ```

2. **Run the container**
   ```bash
   docker run -p 7860:7860 -e OPENAI_API_KEY=your-key-here agent-evaluator
   ```

## 📁 Project Structure

```
agent-evaluator/
├── app.py              # Main Gradio chatbot interface
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── .env              # Environment variables (not in git)
└── README.md         # This file
```

## 🔐 Security

- **Never commit your `.env` file** - it contains your API keys
- Use environment variables for production deployments
- The `.gitignore` file protects sensitive data

## 🧪 Testing Validation Stages

This minimal setup allows you to:
- Test conversational memory
- Validate response quality
- Evaluate agent behavior across multiple turns
- Compare different model configurations

## 📝 Technologies

- **Gradio**: Web interface framework
- **LangChain**: LLM orchestration and memory
- **OpenAI**: Language model provider
- **Docker**: Containerization

## 🤝 Contributing

This is a minimal evaluation framework. Feel free to fork and extend for your specific validation needs.

## 📄 License

MIT License - feel free to use for your chatbot evaluation projects.

---

**Built for simplicity. Focused on validation.**
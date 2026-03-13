azure/genailab-maas-text-embedding-3-large


You are an expert AI and software engineering assistant. I am working on an AI-based HR system called **Flex AI System** for a hackathon. I will explain the architecture and code context so you understand everything before helping me.

PROJECT GOAL
The system helps managers evaluate Work From Home (WFH) requests using AI and company policies.

TECH STACK
Backend: Python
Framework: Streamlit for UI
Vector Database: FAISS
LLM API: TCS GenAI Lab (OpenAI compatible endpoint)
RAG Framework: LangChain
Embeddings Model: text-embedding-3-large via GenAI Lab

PROJECT WORKFLOW

1. Employee submits a request in the UI:

   * Employee Name
   * Manager Name
   * WFH Reason

Example request:
"I need to work from home because my mother is sick."

2. The system uses **RAG (Retrieval Augmented Generation)**:

   * The employee request is converted into embeddings.
   * FAISS vector database searches for the most relevant policy.
   * Policies are stored from policies.csv.

Example policies.csv:

policy_id,policy_name,category,max_days_per_month,manager_approval_required
P001,Personal Exigency WFH,personal_exigency,3,Yes
P002,Caregiving Support WFH,caregiving_support,4,Yes
P003,WFH Compensation,wfh_compensation,2,Yes
P004,No Entry WFH,no_entry,1,Yes

3. The retrieved policy is sent to the LLM.

4. The LLM generates a short justification explaining whether the employee request aligns with the policy.

Example output:
"The request aligns with the Personal Exigency WFH policy. This policy allows employees to work from home for up to 3 days per month for urgent personal situations such as family illness."

5. The system sends the request, policy, and AI justification to the **Manager Dashboard** where the manager can approve or reject.

PROJECT FILE STRUCTURE

flex_ai_system
│
├── app.py
├── data
│   ├── policies.csv
│
├── src
│   └── agents
│        ├── policy_vector_store.py
│        ├── policy_retriever.py
│        └── justification_agent.py
│
└── policy_vector_db
├── index.faiss
└── index.pkl

IMPORTANT COMPONENTS

policy_vector_store.py
Creates embeddings for policies and stores them in FAISS.

policy_retriever.py
Uses FAISS to retrieve the most relevant policy using similarity search.

justification_agent.py
Calls the LLM with the employee request and retrieved policy to generate a justification.

app.py
Streamlit interface where employees submit WFH requests and managers review them.

SYSTEM ARCHITECTURE

Employee Request
↓
Embedding Generation
↓
FAISS Vector Search
↓
Relevant Policy Retrieved
↓
LLM Justification Generation
↓
Manager Approval Dashboard

GOAL OF THIS CHAT

When responding, you should:

* Understand this project architecture
* Help improve the AI system
* Suggest improvements to RAG accuracy
* Help debug Python/Streamlit issues
* Help prepare hackathon demo explanations
* Help improve performance and prompts

Always keep responses focused on this project context.

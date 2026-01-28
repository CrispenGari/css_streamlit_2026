import streamlit as st
import pandas as pd


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Tinashe Crispen Garidzira | AI Researcher",
    layout="wide",
       page_icon="🎓"
)

# ---------------- CUSTOM CSS (Bootstrap-inspired) ----------------
st.markdown("""
<style>
body {
    background-color: #0b1120;
    color: #e5e7eb;
}
h1, h2, h3 {
    color: #0ea5e9;
    margin-bottom: 0.5rem;
}
.section {
    margin-top: 3rem;
    margin-bottom: 3rem;
}
.card {
    padding: 24px;
    border-radius: 14px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.45);
}
.card__small {
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
}
            
.table-container {
    max-height: 420px;
    overflow-y: auto;
}
hr {
    border: 1px solid #1e293b;
}
            ul {
    list-style: none;
    padding-left: 0;
}
ul li {
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------



publications = pd.DataFrame({
    "Title": [
        "Assessing Bi-LSTM Model’s Performance in Identifying AI-Generated Text in Digital Media",
        "Enhanced Fake News Detection with Domain-Specific Word Embeddings: A TorchText-Based Method for News Semantics Representation",
        "A Modified AlexNet Analysis of Canny Edge Detection as a Noise Reduction Method for Lemon Quality Classification",
        "Examining 1D and 2D CNN Architectures in Comparison for Sentiment Analysis in Sequential Data: A Case Study of Spotify Music Reviews",
        "A GraphQL API for Product Recommendation in Women's Clothing Based on Deep Learning Analysis of Product Reviews",
        "A Comparative Analysis of Convolutional Neural Networks, Bi-Directional Gated Recurrent Units, and Bi-Directional Long Short-Term Memory for Sequential Data Processing Using Human Emotions Dataset",
        "Dispatching News Based on Exact Location Using Dispatch (D) App: An Alternative to X (Twitter)",
        "A Rest API to Classify Pneumonia Infection From Chest X-ray Images Using Multi-Layer Perceptron and LeNet",
        "Legal Text Clustering with Bidirectional Gated Recurrent Unit and GloVe Embedding Vectors Using Spectral Clustering Algorithm: An Unsupervised Approach",
        "Detecting Fraudulent Job Postings Using Bi-LSTM-Based Text Classification",
        "Deep Spectro-temporal Embeddings from the M5 CNN with Spectral Clustering for Unsupervised Heartbeat Sound Clustering",
        "Unsupervised Lemon Quality Segmentation Using ResNet50 and Spectral Clustering",
        "A Mobile Application Approach to Deep Learning for Symptom-Based Disease Detection from User Textual",
        "Customer Segmentation in E-Commerce Through Data-Driven Customer Behavior Analysis Employing Unsupervised Machine Learning Models",
        "Deep Learning Driven Threat Detection in Network Traffic Using Multi-Layer Perceptron (MLP) on Public Intrusion Datasets",
        "MobileNetV3-Based Disease Detection from Poultry Faecal Images Using a Mobile-Integrated System"
    ],
    "Authors": [
        "T.C. Garidzira, W.T. Vambe, C. Matobobo",
        "T.C. Garidzira, S. Ngwenya",
        "T.C. Garidzira, W.T. Vambe",
        "C. Matobobo, T.C. Garidzira",
        "T.C. Garidzira, C. Matobobo",
        "W.T. Vambe, T.C. Garidzira",
        "T.C. Garidzira, W.T. Vambe",
        "T.C. Garidzira, W.T. Vambe",
        "T.C. Garidzira, W.T. Vambe",
        "W.T. Vambe, S. Gumbo, T.C. Garidzira",
        "T.C. Garidzira, C. Gurajena",
        "T.C. Garidzira, N. Jere",
        "T.C. Garidzira, C. Matobobo",
        "T.C. Garidzira, C. Matobobo, V.T. Vambe",
        "T.C. Garidzira, V.T. Vambe, C. Matobobo, S. Ngwenya, C. Gurajena",
        "T.C. Garidzira, K. Sibanda, T. Nyashadzashe"
    ],
    "Year": [
        2025, 2025, 2025, 2025, 2024, 2024, 2024, 2023, 2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025
    ],
    "Research Area": [
        "Natural Language Processing",
        "Natural Language Processing",
        "Computer Vision",
        "Natural Language Processing",
        "Recommender Systems",
        "Natural Language Processing",
        "Location-Based Services / NLP",
        "Computer Vision / Healthcare",
        "Natural Language Processing",
        "Natural Language Processing",
        "Computer Vision / Healthcare",
        "Computer Vision / Agriculture",
        "Healthcare / NLP",
        "Data Science / E-Commerce",
        "Network Security / Deep Learning",
        "Computer Vision / Agriculture"
    ],
    "Status": [
        "Published",
        "Published",
        "Published",
        "Published",
        "Published",
        "Published",
        "Published",
        "Published",
        "Published",
        "In Progress",
        "In Progress",
        "In Progress",
        "In Progress",
        "In Progress",
        "Published",
        "Published"
    ]
})

# Order publications by year (descending) and number them
publications = publications.sort_values("Year", ascending=False).reset_index(drop=True)
publications.insert(0, "No.", publications.index + 1)

skills = {
    "Programming": ["Python", "C++", "Java", "JavaScript", "TypeScript"],
    "Frameworks": ["React Native", "Django", "Flask", "Vue.js"],
    "Machine Learning & AI": ["PyTorch", "TensorFlow", "Scikit-learn", "Pandas", "NumPy"],
    "Databases": ["MongoDB", "MySQL", "PostgreSQL"],
    "Cloud & DevOps": ["Firebase", "Kaggle", "Hugging Face", "Docker", "Git"],
    "Soft Skills": ["Communication", "Leadership", "Mentoring"]
}

# ---------------- HEADER / PROFILE ----------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image(
        "me_square.png",
        width=400
    )

with col2:
    st.title("Tinashe Crispen Garidzira")
    st.subheader("Software Developer and AI Researcher")
    st.markdown("""
    <div class="card">
    I am a software developer and AI researcher focused on deep learning, machine learning,
    and software engineering. I build open-source libraries, conduct academic research,
    and develop full-stack applications using modern technologies.

    My research interests include natural language processing, computer vision,
    recommender systems, and unsupervised learning. I work extensively with PyTorch,
    Kaggle, and Hugging Face datasets and actively contribute to real-world AI projects.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Skills & Expertise")

cols = st.columns(3)
i = 0
for category, items in skills.items():
    with cols[i % 3]:
        st.markdown(f"<div class='card__small'><h4>{category}</h4>", unsafe_allow_html=True)
        for skill in items:
            st.write(f"- {skill}")
        st.markdown("</div>", unsafe_allow_html=True)
    i += 1
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- PUBLICATIONS ----------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Research Publications")

st.markdown("""
<div class="card">
The following table lists my peer-reviewed publications and ongoing research work,
ordered by year.
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='table-container'>", unsafe_allow_html=True)
st.dataframe(publications, width='stretch', hide_index=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# ---------------- CONTACT ----------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Contact Information")

st.markdown("""
<div class="card">
<ul>
    <li><b>Email:</b> crispengari@gmail.com</li>
    <li><b>Website:</b> <a href="https://www.crispengari.com" target="_blank">https://www.crispengari.com</a></li>
    <li><b>GitHub:</b> <a href="https://github.com/crispengari" target="_blank">https://github.com/crispengari</a></li>
    <li><b>Location:</b> South Africa</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

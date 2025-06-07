# Large-scale Data Analysis using MapReduce – Cloud Computing

This project analyzes social media data (e.g., Twitter, Instagram, Facebook posts) to determine the sentiment (positive, negative, neutral) expressed in the text of the posts.  
This project aims to assess public opinion, emotional trends, or how individuals feel about various topics across different regions and time periods. 📊

---

## 📂 Files

- `preprocess.py` – Preprocessing script to clean the dataset  
- `mapper.py` – MapReduce mapper script  
- `reducer.py` – MapReduce reducer script  
- `sentimentanalysis_output.txt` – Output file from HDFS  
- `sentiment_distribution.py` –  Python script to parse results and visualize sentiment distribution  
- `sentiment_distribution.csv` – CSV result of the sentiment distribution  
- `sentiment_distribution.png` – Sentiment distribution plot  

---

## 🛠️ Steps to Set Up Hadoop in Ubuntu

📚 Refer: [Install Hadoop on Ubuntu – PhoenixNAP Guide](https://phoenixnap.com/kb/install-hadoop-ubuntu)

1. ☕ Install JDK on Ubuntu  
2. 🔑 Set up Hadoop User and configure SSH  
3. 📥 Download and install Hadoop on Ubuntu  
4. 🖥️ Single Node Hadoop deployment  
5. 💾 Format HDFS NameNode  
6. ▶️ Start Hadoop cluster  
7. 🌐 Access Hadoop from Browser  

---

## 📥 Download and Clean Data

- 🌐 Download the dataset from Kaggle:  
  [Social Media Sentiments Analysis Dataset](https://www.kaggle.com/datasets/kashishparmar02/social-media-sentiments-analysis-dataset?resource=download)

- 🧹 Run `preprocess.py` to clean the dataset:
```bash
python3 preprocess.py 

## 🚀 Steps to Run

### 📤 Upload Dataset to HDFS

```bash
hdfs dfs -mkdir -p /sentimentanalysis_input
hdfs dfs -put sentimentanalysis_clean.csv /sentimentanalysis_input/

### 🏃 Run MapReduce Job

```bash
hadoop jar /home/hdoop/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
  -files mapper.py,reducer.py \
  -input /sentimentanalysis_input/sentimentanalysis_clean.csv \
  -output /sentimentanalysis_output \
  -mapper mapper.py \
  -reducer reducer.py

### 📥 Get Output from HDFS

```bash
hdfs dfs -get /sentimentanalysis_output/part-00000 sentimentanalysis_output.txt

### 📊 Visualize with Python

```bash
python3 sentiment_distribution.py

### 🛠️ Setup Python Requirements (If not installed)

```bash
sudo apt install python3-pip
pip3 install --user pandas matplotlib


### 🎉 Results

```bash
# Output file
sentiment_distribution.csv

# Visualization image
sentiment_distribution.png


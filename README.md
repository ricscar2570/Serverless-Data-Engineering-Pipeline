# 🚀 Serverless Data Engineering Pipeline

[![AWS]([https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws&style=flat-square)](https://aws.amazon.com/](https://github.com/ricscar2570/portfolio/blob/main/Serverless%20Data%20Engineering%20Pipeline/Serverless.png?raw=true)) 
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Contributors](https://img.shields.io/github/contributors/your-repo?color=green&style=flat-square)](https://github.com/your-repo)

> 🛠️ Una pipeline di data engineering serverless scalabile, sicura e progettata per applicazioni IoT e Machine Learning.

---

## 🌟 **Caratteristiche Principali**
✔️ **Ingestione in tempo reale** dei dati tramite endpoint REST.  
✔️ **Trasformazione automatica** dei dati grezzi in dataset strutturati.  
✔️ **Machine Learning** con SageMaker per predizioni in tempo reale.  
✔️ **Dashboard interattiva** per il monitoraggio e la visualizzazione dei dati.  
✔️ **Serverless** e altamente scalabile grazie all'architettura AWS.  

---

## 🏗️ **Architettura del Progetto**

### **Diagramma dell'Architettura**

```mermaid
sequenceDiagram
    participant User as Dispositivo/Utente
    participant LambdaIngest as Lambda Ingestione Dati
    participant S3 as S3 Archiviazione Dati
    participant Glue as Glue ETL
    participant SageMaker as SageMaker
    participant Dashboard as Dashboard React

    User->>LambdaIngest: Invio Dati (POST)
    activate LambdaIngest
    LambdaIngest->>S3: Salva dati grezzi
    deactivate LambdaIngest
    
    S3->>Glue: Trigger ETL Job
    activate Glue
    Glue-->>S3: Salva dati trasformati
    deactivate Glue
    
    S3->>SageMaker: Fornisce dati per l'addestramento
    activate SageMaker
    SageMaker-->>S3: Salva modello addestrato
    deactivate SageMaker

    User->>SageMaker: Richiesta di predizioni
    activate SageMaker
    SageMaker->>User: Restituisce predizione
    deactivate SageMaker

    User->>Dashboard: Visualizza dati e predizioni
    activate Dashboard
    deactivate Dashboard
```

1. **AWS Lambda**: Funzioni per ingestione dati e inferenze in tempo reale.
2. **Amazon S3**: Archiviazione per dati grezzi, trasformati e dataset ML-ready.
3. **AWS Glue**: Trasformazione e preparazione dei dati per machine learning.
4. **Amazon SageMaker**: Addestramento e distribuzione del modello ML.
5. **React Dashboard**: Interfaccia utente per visualizzare e monitorare i dati.

---

## 🧩 **Componenti del Progetto**

### **1. Lambda Functions**  
- 📥 **Data Ingestion**: Raccoglie i dati e li archivia in S3.  
- 🤖 **Prediction Service**: Restituisce predizioni in tempo reale da SageMaker.

### **2. Glue ETL Scripts**  
- 🔄 **Transform Data**: Pulisce e struttura i dati grezzi.  
- 🧹 **Prepare ML Dataset**: Genera dataset CSV per l'addestramento ML.

### **3. SageMaker**  
- 🏋️ **Training**: Addestra un modello di regressione lineare.  
- ⚡ **Endpoint Deployment**: Distribuisce il modello per inferenze in tempo reale.  

### **4. Front-End**  
- 📊 **Dashboard**: Visualizza predizioni e distribuzioni dei dati con grafici interattivi.  
- 📁 **Upload Multi-file**: Permette il caricamento simultaneo di più file.

---

## 🌈 **Tecnologie Utilizzate**
![AWS](https://img.shields.io/badge/AWS-100%25-orange?logo=amazonaws&style=flat-square)
![React](https://img.shields.io/badge/React.js-UI-blue?logo=react&style=flat-square)
![Python](https://img.shields.io/badge/Python-ETL-yellow?logo=python&style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-brightgreen?logo=javascript&style=flat-square)

- **AWS Services**: Lambda, S3, Glue, SageMaker, Step Functions.  
- **Framework**: React.js per la dashboard interattiva.  
- **Linguaggi**: Python (ETL, Lambda), JavaScript (Frontend).  

---

## 🚀 **Come Funziona?**


```
    Raccolta dati: I dispositivi inviano dati a un endpoint gestito da Lambda.
    Archiviazione: I dati vengono salvati in S3.
    ETL: Glue trasforma e prepara i dati per il machine learning.
    Addestramento: SageMaker addestra un modello con i dati preparati.
    Predizioni: Lambda invoca l’endpoint SageMaker per predizioni in tempo reale.
    Visualizzazione: La dashboard React mostra i dati e le predizioni.

📂 Struttura della Cartella

├── src/
│   ├── lambda/
│   │   ├── data_ingestion.py
│   │   ├── prediction_service.py
│   ├── glue/
│   │   ├── transform_data.py
│   │   ├── prepare_ml_dataset.py
│   ├── sagemaker/
│   │   ├── train_model.py
│   │   ├── deploy_model.yaml
│   ├── frontend/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── Dashboard.js
│   │   │   │   ├── Upload.js
│   │   │   ├── App.js
│   │   │   ├── index.js
├── README.md
├── LICENSE

```

📈 Grafici e Visualizzazioni
Predizioni nel Tempo

Distribuzione dei Dati

🔧 Setup
1. Requisiti

    AWS CLI: Configurato con credenziali valide.
    Node.js: Per il frontend React.
    Python 3.x: Per script ETL e Lambda.

2. Deployment

    Clonare il repository:

git clone https://github.com/your-repo/serverless-pipeline.git
cd serverless-pipeline

Configurare AWS CLI:

aws configure

Installare le dipendenze:

    Lambda e Glue:

pip install -r requirements.txt

Frontend:

    cd frontend
    npm install

Deploy CloudFormation:

aws cloudformation deploy --template-file template.yaml --stack-name serverless-pipeline

Avviare il Frontend:

    npm start

📌 Esempi di Utilizzo
Richiesta di Ingestione Dati

curl -X POST -H "Content-Type: application/json" -d '{"device_id": "123", "value": 42}' https://your-api-endpoint/data-ingestion

Richiesta di Predizione

curl -X POST -H "Content-Type: application/json" -d '{"feature_value": 50}' https://your-api-endpoint/predict

🤝 Contribuire

Contribuire è semplice! Segui questi passi:

    Fork il repository.
    Crea un nuovo branch: git checkout -b feature-nuova-funzionalità.
    Fai il commit delle modifiche: git commit -m "Aggiunta nuova funzionalità".
    Fai un push al branch: git push origin feature-nuova-funzionalità.
    Apri una Pull Request.

📝 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file LICENSE per maggiori dettagli.
📧 Contatti

Hai domande o suggerimenti? Contattaci!
📧 Email: ricscar@gmail.com
🌐 Website: riccardoscaringi.eu


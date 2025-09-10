# color-generator

## 🎨 ColorPalette Semantic Generator 

> Générez des palettes de couleurs cohérentes en fonction du sens ou de l’ambiance que vous recherchez — grâce à l’IA et aux embeddings sémantiques.

 
## 🧠 Concept 

Ce projet permet de générer ou rechercher des palettes de couleurs non pas par codes hexadécimaux ou noms techniques, mais par mots-clés sémantiques comme : 

 >   "calme océan printanier"  
 >   "énergie électrique"  
 >   "élégance royale"  
 >   "chaud coucher de soleil"  
     

Grâce à des embeddings de phrases (via `sentence-transformers`), le système compare la similarité sémantique entre votre requête et des descriptions de palettes pré-enregistrées, puis vous retourne les meilleures correspondances.  

## ✨ Fonctionnalités 

*    🔍 Recherche sémantique de palettes par description textuelle
*    🖌️ Affichage visuel des couleurs dans le terminal (avec codes hex et noms)
*    📦 Base de données intégrée de palettes thématiques
*    🧩 Extensible : ajoutez vos propres palettes et descriptions
*    🖥️ Compatible avec les terminaux TrueColor (24-bit)
     

 
## 🚀 Installation 
### Prérequis 

    Python 3.8+
    pip
    Terminal supportant les couleurs 24-bit (vérifiez avec ce test )
     

### Étapes 
```bash
# 1. Clonez le dépôt
git clone https://github.com/clement-massit/color-generator
cd color-generator

# 2. Créez un environnement virtuel (optionnel mais recommandé)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# 3. Installez les dépendances
pip install -r requirements.txt
```
 
### Fichier requirements.txt 

```txt
huggingface-hub==0.34.4
sentence-transformers==5.1.0
numpy==2.3.3
```  

## 🧪 Utilisation 
### Exemple simple 
 
```bash
python app.py
```
 
### Résultat attendu dans le terminal 


### 🎨 Meilleure correspondance : "Snow" (similarité: 0.77)

> Snow: #FFFAFA  0.77  
> Ultramarine: #3F00FF  0.73  
> Wine: #722F37  0.73  
> Zinc: #7E7F9A  0.76  
> Tomato: #FF6347  0.76  
> Wine: #722F37  0.74
 


## 💡 Extensibilité 

Vous pouvez : 

> Ajouter de nouvelles palettes dans palettes.json  
> Changer le modèle d’embedding (ex: all-mpnet-base-v2 pour plus de précision)  
> Exporter les résultats en PNG, CSS, ou Figma tokens  
> Intégrer une interface web (Streamlit, Gradio…)  
     
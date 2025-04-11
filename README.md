# mehndi_designs
# 🌸 Floral Mehndi Design Generator
GoodBye to searching long web pages to select Hina designs , welocme Floral Mehndi Design Generator
This Streamlit application allows users to generate beautiful Mehndi (Henna) designs tailored to their preferences using Google Gemini's image generation model.

---

## 🚀 Features

- Choose from multiple Mehndi styles: Pakistani, Arabic, Indian, Bridal, Tattoo, etc.
- Select the age range of the hand (e.g., toddler, adult, senior).
- Specify the occasion: wedding, festival, party, etc.
- Choose the complexity of the design (1 to 5).
- Add custom user prompts for specific preferences.
- Generate multiple AI-designed Mehndi images.
- Ensures proper hand anatomy with no overlapping or double fingers.
- Automatically converts transparent images to have white backgrounds.

---

## 🧰 Requirements

- Python 3.8+
- Streamlit
- Google Generative AI SDK
- PIL (Python Imaging Library)

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/mehndi_designs.git
   cd mehndi-generator
   ```
![image](https://github.com/user-attachments/assets/4f9affa6-5dac-45db-b566-eebf662ae73e)
![image](https://github.com/user-attachments/assets/f0fad538-09e4-405c-a74c-4c3f22334ab8)


---
## 🐳 Docker Commands Details:
```bash
docker build -t mehndi-generator : For building the image
```
  ![image](https://github.com/user-attachments/assets/11dca29b-3aaf-4206-8b06-e943bca624f3)
  
```bash
docker tag mehndi-generator zainabkhan999/mehndi-generator:v1   Tag your image with your Docker Hub username and the desired repository name
docker push zainabkhan999/mehndi-generator:v1 :Push the image to Docker Hub
```
  ![image](https://github.com/user-attachments/assets/7cd9c436-b225-4806-b3fa-cd66f5bfd253)
  
-  Creating git repo
  ```bash
      echo "# goodevening" >> README.md
      git init
      git add README.md
      git commit -m "first commit"
      git branch -M main
      git remote add origin https://github.com/zainikhan999/goodevening.git
      git push -u origin main
   ```
---
 ```bash
  docker run -p 8501:8501 zainabkhan999/mehndi-design:v1
  ```
![image](https://github.com/user-attachments/assets/82a17039-8ffe-4895-b4cf-58e5a1fb9b66)



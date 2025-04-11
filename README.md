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
- Building an image:
```bash
docker build -t mehndi-generator : For building the image
```
  ![image](https://github.com/user-attachments/assets/11dca29b-3aaf-4206-8b06-e943bca624f3)

- Push Image to Docker Hub:
  Tag your image with your Docker Hub username and the desired repository name
```bash
docker tag mehndi-generator zainabkhan999/mehndi-generator:v1
```
```bash 
docker push zainabkhan999/mehndi-generator:v1 
```
Push the image to Docker Hub
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
## Part 2 Docker Containers with commands
- List running containers.
  ``` bash
  docker ps
  ```
- Stop a running container.
  ``` bash
  docker stop <container>
```
- Remove a stopped container.
 ```bash
  docker rm <container>
  ```
- Display detailed information about a container.
 ```bash
  docker inspect <container>
  ```
- Start a stopped container.
``` bash
docker start <container>
```
- View logs from a container.
``` bash
docker logs <container>
```
-Show real-time resource usage of containers.
``` bash
docker stats
```
- Run a command inside a running container (e.g., bash shell).
``` bash
docker exec -it <container> <command>
```
- Attach to a running container's terminal.
```bash
docker attach <container>

```
- Create a new image from a container's current state.
``` bash
docker commit <container> <image-name>
```
- Copy files/folders between container and host.
``` bash
docker cp <container>:<path> <host-path>
```
- Show processes running inside a container.
``` bash
docker top <container>
```
- Pause all processes in a container.
``` bash
docker pause <container>
```
- Resume a paused container.
``` bash
docker unpause <container>
```
- Rename an existing container.
``` bash
docker rename <old-name> <new-name>
```
- Block until the container stops and return its exit code.
``` bash
docker wait <container>
```
- List port mappings for a container.
``` bash
docker port <container>
```
- Restart a running container.
``` bash
docker restart <container>
```
- Update resource limits of a running container.
``` bash
docker update <container> --memory 500m
```
![image](https://github.com/user-attachments/assets/82a17039-8ffe-4895-b4cf-58e5a1fb9b66)



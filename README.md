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
  ![image](https://github.com/user-attachments/assets/4a93d7df-c320-49bb-b02f-03dcee5dd1d2)

- Stop a running container.
  ``` bash
  docker stop <container>
  ```
  ![image](https://github.com/user-attachments/assets/3b0a9562-fed5-42be-8679-ff050f058d3b)

- Remove a stopped container.
  ```bash
  docker rm <container>
  ```
  ![image](https://github.com/user-attachments/assets/bdad7b7d-3a14-4bfd-87b5-021669640b8a)

- Display detailed information about a container.
 ```bash
  docker inspect <container>
  ```
![image](https://github.com/user-attachments/assets/f649d797-544c-44cb-8154-629335c44be0)

- Start a stopped container.
``` bash
docker start <container>
```
![image](https://github.com/user-attachments/assets/36e871f1-98a2-47cf-8d93-daca0c3f0d53)

- View logs from a container.
``` bash
docker logs <container>
```
![image](https://github.com/user-attachments/assets/c4398577-73bf-44fe-8acf-5ac4423e4ad8)

-Show real-time resource usage of containers.
``` bash
docker stats
```
![image](https://github.com/user-attachments/assets/474d9160-6528-42e1-9e5f-44958a9c9dff)

- Run a command inside a running container (e.g., bash shell).
``` bash
docker exec -it <container> <command>
```
![image](https://github.com/user-attachments/assets/34237ccf-cdbe-40ed-9d4a-5aaeee6082bc)

- Attach to a running container's terminal.
```bash
docker attach <container>
```
![image](https://github.com/user-attachments/assets/fc6b7a9d-e2ae-4021-b6ee-f651546b61a0)

- Create a new image from a container's current state.
``` bash
docker commit <container> <image-name>
```
![image](https://github.com/user-attachments/assets/b3b3cf2b-fd7c-4d18-8c80-92da5847a48c)

- Copy files/folders between container and host.
``` bash
docker cp <container>:<path> <host-path>
```
![image](https://github.com/user-attachments/assets/3f4fd55a-ee22-4764-a13e-912e7633e498)

- Show processes running inside a container.
``` bash
docker top <container>
```
![image](https://github.com/user-attachments/assets/9bb50873-6c6c-499c-94b9-96a5f0a4e699)

- Pause all processes in a container.
``` bash
docker pause <container>
```
![image](https://github.com/user-attachments/assets/0c9c2e9f-5ce5-4b06-83ab-a2e04241c11b)

- Resume a paused container.
``` bash
docker unpause <container>
```
![image](https://github.com/user-attachments/assets/fa0c6d43-878e-49ca-811e-9a29fbdd2be0)


- Rename an existing container.
``` bash
docker rename <old-name> <new-name>
```
![image](https://github.com/user-attachments/assets/6887d811-cfad-4fc8-bb9f-3c3f0a34508f)

- Block until the container stops and return its exit code.
``` bash
docker wait <container>
```
![image](https://github.com/user-attachments/assets/08a96622-6310-4c7d-a189-8095dfe79a8c)


- List port mappings for a container.
``` bash
docker port <container>
```
![image](https://github.com/user-attachments/assets/07e4e9c8-5d91-4f65-a01b-d3db0f4a7394)


- Restart a running container.
``` bash
docker restart <container>
```
![image](https://github.com/user-attachments/assets/df29c217-f6a7-4695-be40-d73c5365754b)

- Update resource limits of a running container.
``` bash
docker update <container> --memory 500m
```
![image](https://github.com/user-attachments/assets/df8efc26-6426-4b81-b2d4-b30f50effc4a)

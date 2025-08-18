# Bicycle Rental Project

**Student:** Marko Nikolić  
**Index:** E2 47/2024  

---

## Project Overview

This project consists of **one central bicycle rental system** and **three local bicycle rental systems**:

- **Central system:** Tracks users and their rentals.  
- **Local systems:** Track bicycles and their rentals.  

**Docker Images:**  
- Central system: [markoni01/central-bicycle-rental](https://hub.docker.com/r/markoni01/central-bicycle-rental)  
- Local systems: [markoni01/local-bicycle-rental](https://hub.docker.com/r/markoni01/local-bicycle-rental)  

---

## Architecture

<p align="center">
  <img src="https://github.com/user-attachments/assets/83068866-8e46-4841-9e28-3ba31f259cd8" alt="Bicycle Rental Architecture" width="400"/>
</p>

The architecture includes:  
- 1 Central Bicycle Rental System  
- 3 Local Bicycle Rental Systems (NS, SU, KG)  

---

## Goals

The main goals of the project were:

1. Create a **GitHub workflow** to automate image builds and push them to Docker Hub.
2. Deploy all applications using **Docker Compose**.  
3. Deploy all applications using **Kubernetes**.

<p align="center">
  <img alt="GitHub_Invertocat_Logo svg" src="https://github.com/user-attachments/assets/57309762-3556-475c-b331-c4fa8561d167" height="200"/>
</p>

<p align="center">
  <img alt="Docker_logo svg" src="https://github.com/user-attachments/assets/706c437a-2881-413f-8e80-2b5091a02fe1" height="130"/>
</p>


<p align="center">
  <img alt="Kubernetes_logo_without_workmark svg" src="https://github.com/user-attachments/assets/e4218537-a592-46f4-b839-f48f3c46f0dc" height="200"/>
</p>



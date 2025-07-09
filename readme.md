# MobilTelesco: A Smartphone-Based Astrophotography Dataset

MobilTelesco is a pioneering, open-access dataset featuring astrophotography images captured using **affordable smartphone setups**. This project explores how modern consumer devices—paired with basic stabilization techniques—can democratize sky observation and contribute to citizen-led astronomical research and machine learning applications.

> Developed entirely by Shan Parmar, an undergraduate researcher from Marwadi University, India, MobilTelesco reflects a passion-driven initiative to make astrophotography more inclusive and computationally accessible.

---

## 🌌 Overview

Smartphone sensors have advanced to the point where, with some patience and long-exposure apps, they can image stars, constellations, and even the Milky Way. MobilTelesco documents this capability across multiple nights, locations, and devices, showcasing what can be achieved with:
- Minimal budget
- No professional telescope
- Passion for the night sky and open-source science

This dataset was used in the paper **“Evaluating Deep Learning Models on Smartphone-Based Astrophotography”**, accepted at **CAIP 2025** (Computer Analysis of Images and Patterns).

---

## 📁 Dataset Contents

MobilTelesco/
├── images/ # Main astrophotography dataset (JPG, PNG)
│ ├── IMG_001.jpg
│ ├── IMG_002.jpg
├── labels.csv # (Optional) Metadata: device, timestamp, exposure, location
├── metadata.json # Extended metadata (where available)
├── LICENSE # CC-BY 4.0
└── README.md # Project overview, citation, usage

yaml
Copy
Edit

---

## 🧾 Metadata Description

| Field        | Description                                 |
|--------------|---------------------------------------------|
| filename     | Image file name (e.g., IMG_003.jpg)         |
| timestamp    | UTC datetime of capture                     |
| location     | Approximate location (City or GPS, optional)|
| phone_model  | Smartphone make/model used                  |
| exposure     | Exposure time or app used (e.g., NightCap)  |
| sky_target   | Visible objects (e.g., Milky Way, Orion)    |

---

## 💡 Use Cases

MobilTelesco can serve multiple research and outreach purposes:
- 📸 **Low-Cost Astronomy Education** – For schools or institutions lacking telescope access
- 🤖 **Computer Vision & ML Training** – Train models for star detection, sky enhancement
- 🌍 **Citizen Science & Outreach** – Promote accessible science across developing regions
- 📊 **Comparative Benchmarking** – Compare smartphone results with professional telescopes

---

## 📜 License

This dataset is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  
You are free to:
- Use, share, and adapt the data
- Even for commercial purposes  
**But you must give appropriate credit** to the dataset author.

---

## 📚 Citation

If you use this dataset in your work, please cite:

Shan Parmar. (2025). MobilTelesco: A Smartphone-Based Astrophotography Dataset. Zenodo. https://doi.org/xxxxx

yaml
Copy
Edit

> 📌 Zenodo DOI will be updated once uploaded and published.

---

## 🚀 Background & Motivation

As an undergraduate with limited access to astronomical hardware, I was curious: *What can a smartphone see of the universe?*  
This dataset was born from dozens of night sessions under Indian skies, using nothing but:
- A smartphone
- A tripod
- The curiosity to explore

This project also highlights the importance of **open data**, **low-resource innovation**, and **inclusive research tools** in STEM.

---

## 🧠 Related Work

This dataset was used in:
- **"Evaluating Deep Learning Models on Smartphone-Based Astrophotography"**, CAIP 2025  
(Accepted paper exploring CNN-based enhancement of smartphone night sky images.)

---

## 🤝 Contributing & Contact

I welcome:
- Collaborations on image analysis or model training
- Contributions of new smartphone images to expand the dataset
- Educational or citizen science outreach projects

📬 **Shan Parmar**  
📧 Email: *yourname@domain.com*  
🌐 Website: [shanparmar.in](https://yourwebsite.com)  
GitHub: [github.com/yourusername](https://github.com/yourusername)

---

## 🖼️ Preview

![MobilTelesco Logo](mobiltelesco-logo.png)  
*“A telescope in your pocket. The universe on your screen.”*

---

## 🙏 Acknowledgements

Special thanks to:
- Open-source communities enabling computational astronomy
- The rural night skies of Gujarat for providing dark sky conditions
- Anyone who's ever pointed their phone at the stars and wondered

---

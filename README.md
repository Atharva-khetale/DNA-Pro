# DNA-Pro
Here's a well-structured `README.md` file for your DNA-to-Protein GUI application written in Python. This documentation includes purpose, usage, dependencies, and features in a clear and professional format:

---

# 🧬 DNA to Protein Converter GUI

This Python application provides a graphical user interface (GUI) to convert DNA strands into mRNA and subsequently into Protein sequences using the **Biopython** library. It simulates a simple **bioinformatics tool** for educational and demonstration purposes.

> **Bonus:** Includes fun features like a turtle-based drawing and placeholder for solar system simulation!

---

## 🚀 Features

* 🌱 Convert DNA to mRNA and Protein sequence using **Biopython**
* 💡 Progress bar animation during conversion
* 🧬 Interactive and user-friendly **Tkinter GUI**
* 🌀 Fun turtle graphics drawing
* 🌌 Menu for future expansion (like solar system visual)

---

## 🛠️ Requirements

Make sure you have the following Python packages installed:

```bash
pip install biopython
```

This app uses:

* `tkinter` (standard with Python)
* `turtle` (standard with Python)
* `biopython`

---

## 🧪 How It Works

1. Enter a valid DNA strand (e.g., `ATGCGTAC`).
2. Click on **"FIND"**.
3. The app:

   * Transcribes the DNA into mRNA.
   * Translates mRNA into a Protein sequence.
   * Displays results in their respective fields.
4. Optional fun:

   * Click menu → **"test"** to launch turtle drawing.
   * Click menu → **"mrna"** to open an MRNA-themed window.
   * "Solar system" option is listed but not yet implemented.

---

## 🧬 Core Libraries Used

* **Biopython**: For `transcribe()` and `translate()` functions.
* **Tkinter**: GUI building.
* **Turtle**: Fun visual simulation.

---

## 📂 Project Structure

```plaintext
project/
│
├── main.py           # Your main application code (provided above)
├── start.py          # Contains `solarsytem` function (placeholder or future expansion)
├── README.md         # This documentation
```

## 📜 License

This project is open for educational and non-commercial use. Modify and expand freely!

---

## 🧠 Future Ideas

* Add validation for nucleotide sequences.
* Visualize codon tables or translation process.
* Complete the "Solar System" simulation.

---

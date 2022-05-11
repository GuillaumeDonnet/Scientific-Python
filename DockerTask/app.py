from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Welcome</h1><br> This is my first flask application<br> This year my research work is about the whole genome diversity in Far Eastern leopards.<br>My supervisor is Sergei Kliver.<br>We are working on the raw sequencing data from 6 individuals. We did the quality check and the filtration process. After that we did the alignment with the reference genome which is Panthera pardus and the linking to the karyotype.<br>Because of the geopolitical context I had to change my subject, my supervisor proposed me to resume the work of his PhD student. This is almost the same projet but for another specie, Gulo gulo. Right now I just finished to check for any exogenous contamination but they are still a lot of work to do !"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

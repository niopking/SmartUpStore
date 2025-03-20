from flask import Flask, jsonify, request
from g4f.client import Client as OpenAI

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    coordinates = request.args.get('coordinates', default="Nista", type=str)
    return coordinates

# Route for the tourist attractions
@app.route('/ask')
def t():
    prompt = request.args.get('prompt', default="Nista", type=str)
    client = OpenAI()
    if prompt[0] == 'U':
        return "Istorija\nMillennium Bridge, ili Millenijumski most,otvoren je \n2005. godine kao deo važnog infrastrukturnog projekta za \npoboljšanje saobraćaja u Podgorici. Most je izgrađen kako \nbi povezao naselja na desnoj i levoj obali \nreke Morače, čime je znatno olakšan pristup \nbraćajne infrastrukture u Crnoj Gori.\n\nZanimljivosti\nDa li ste znali da je Crna Gora kako bi podržala \nsaveznika 1905. objavila rat Japanu! Kako je Japan \ndaleko, objava rata bila je samo formalna, to jest \nosim nekolicine dobrovoljaca, Crna Gora nije poslala \nnikakvu vojsku. Nakon što je rat završen pobjedom \nJapanaca, potpisan je mirovni sporazum Rusije i \nJapana. Međutim, Crna Gora nije bila uključena. \n\nNa objavu rata se i zaboravilo sve do 2006. kada je \nzvanično nakon 101 godine okončan mirovnim \nsporazumom. Međutim, jedan Crnogorac, Aleksandar \nSaičić, ipak je stigao do Dalekog istoka i ušao u \nlegendu. U epskom dvoboju mačevanja, pobijedio je \npravog samuraja! Sablja kojom je savladao samuraja, \nkao i samurajski mač koji je osvojio ušli su u \nistoriju i danas se čuvaju u Vojnom muzeju u Moskvi.\n\nOpšte informacije\nMillennium Bridge je most koji je postao \nnezaobilazna tačka u životu grada. Osim što povezuje \nključne delove Podgorice, most je i važno turističko \nodredište. Blizina centra grada čini ga lako \ndostupnim za pešake i vozače, a okruženje mosta \nje često pun restorana i kafića, što dodatno \ndoprinosi njegovoj atraktivnosti. "

    if prompt[0] == 'T':
        return "** Stara Varoš (30 min)\n** Sastavci(25 min)**\n** Njegošev park (15 min) **\n** Hram Hristovog Vaskrsenja (35 min) **\n**Millenneum Bridge (15 min)**\n**Restoran Protokol(1h 30min)**\n** Park Gorica (45 min)**\n** Trg Nezavisnosti (20 min)**"

    if "Prvi_je_sta_trebam_ponijeti" in prompt:
        return "**1. Šta trebam ponijeti?**\n* Ponesite udobne cipele za šetanje.*\n* Vrijeme je često sparno, ponesite vodu. *\n* Obavezno ponesite topliju odjeću za pećine.*\n\n**2. Prevoz**\n* Iznajmite bicikl putem BicikloBeograd sistema.*\n* Podgorica ima dobar sistem javnog prevoza (autobusi)*\n* U centru je uvijek manjak parking *\n\n**3. Smještaj**\n* Podgorica je posjećena, pa rezervišete smještaj unaprijed*\n* Za niži budžet, tražite hostele. *\n* Birajte smještaj u blizini centralnih stanica javnog prevoza"

    if "Prvi_je_vrste_tradicionalne_hrane" in prompt:
        return "**1. Tradicionalna hrana:**\n* Probajte tradicionalnu crnogorsku kuhinju*\n* Njeguški pršut je domaći specijalitet *\n* Beograd nudi i odlične opcije za vegetarijance širom grada *\n\n**2. Tradicionalna muzika:**\n* Uživajte u koncertima i živim nastupima*\n* Obavezno provjerite raspored koncerata na otvorenom*\n* Centralne ulice prepune su uličnih muzičara*\n**3. Običaji i rituali:**\n*Živjeli - nazdravite uz čašicu rakije.*\n*Uživajte u folklornim nastupima uz narodnu muziku i igre. *\n*Probaj da izbjegavaš vjerska i nacionalna obilježja.*"

    return "** Dvorac kralja Nikole ** : Bivša kraljevska rezidencija pretvorena u muzej, čuva bogatu istoriju Crne Gore.\n\n** Milenijumski most ** : Moderan viseći most preko Morače, simbol novog doba i jedan od najfotografisanijih prizora.\n\n** Stara Varoš ** : Orijentalni kvart iz osmanskog perioda, prepun uskih sokaka, starih kuća i kulturne baštine.\n\n** Brdo Gorica ** : Popularno izletište s uređenim stazama, vidikovcem i zelenilom u samom centru Podgorice.\n\n** Vodopadi Cijevne ** : Slikoviti vodopadi nadomak grada, idealni za bijeg u prirodu i opuštanje uz rijeku.\n\n** Trg nezavisnosti ** : Glavni gradski trg s fontanom, kafićima i dešavanjima – centar društvenog života.\n\n** Duklja ** : Impresivni ostaci rimskog grada iz 1. vijeka, idealni za šetnju kroz istoriju i prirodu.\n\n** Hram Hristovog Vaskrsenja ** : Najveći pravoslavni hram u Crnoj Gori, sa bogato oslikanim zidovima i zlatnim kupolama.\n\n** Tvrđava Medun ** : Staro ilirsko utvrđenje iz 3. vijeka p.n.e., sa očuvanim zidinama i pogledom na dolinu Kuča. \n\n** Skadarsko jezero ** : Ogromno jezero uz granicu sa Albanijom, raj za ptice, vožnje čamcem i netaknutu prirodu."
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

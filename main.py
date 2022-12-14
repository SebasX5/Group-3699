# Course: CST205, Multimedia Design & Programming
# Abstract: Flask gardening website
# Authors: Antonio Barron, Mursal Mousumi, Sebastian Santoyo
# Date: December 16, 2022
# Mursal: worked on home page, regions page, Zone 1-4 files and css file
# Antonio: worked on Zone 5-8 files
# Sebastian: worked on Zone 9-12 files, set up the dictionary function

# Sources cited where appropriate
# https://gilmour.com/planting-zones-hardiness-map#zone9

# https://github.com/SebasX5/Group-3699 


from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

#vegDict: contain all vegetable, based on name input info onto template 
#dictionary of lists with following information [title name, image, water description]
vegDict = {   
    #zone 1
    "beans" : ["Beans", "beans.jpeg", "Irrigate beans immediately after planting. Keep the seed bed moist, but not soggy, for the first week until germination occurs. Reduce watering to once every three days after the first week. Water as needed after beans become established, usually about twice a week."],
    "lettuce" : ["Lettuce", "lettuce.jpeg", "Lettuce has shallow roots, so plants need consistent watering. Check at least twice a week and water if the soil is dry down to 1 inch deep. Containers of lettuce need to be watered more frequently than garden beds, especially in the summer."],
    "potato" : ["Potato", "potato.jpeg", "Potatoes need between 1-2 inches of water per week;"],
    #zone 2
    "mustardGreen" : ["Mustard Greens", 'mustardGreen.jpeg', "Mustard greens need 2 inches (5 cm.) of water a week."],
    "onion" : ["Onion", 'onion.jpeg', "Onions need about 1 inch of water per week"],
    #zone 3
    "asparagus" : ["Asparagus", "asparagus.jpeg", "Asparagus patches should receive at least one inch of water every week"],
    "celery" : ["Celery", "celery.jpeg", "It needs between 1 and 1.5 inches of water per week"],
    "cucumber" : ["Cucumber", "cucumber.jpeg", "They need at least one inch of water per week (or more, if temperatures are particularly high)"],
    #zone 4
    "pumpkin" : ["Pumpkin", "pumpkin.jpeg", "Pumpkins need 1 inch of water per week. Water deeply, in the morning and on very hot afternoons, especially during fruit set. Avoid watering foliage and fruit unless it's a sunny day. Dampness invites rot and disease."],
    
    #zone 5
    
    #zone 6
    "butterLettuce" : ["Butter Lettuce", "butterlettuce.jpeg" , "Water lightly every day to maintain moisture. To promote quick growth, water a little bit every day???or every other day after the seeds sprout. This will cause the lettuce to have a tastier, sweeter flavor."], 
    #zone 7
    "arugula" : ["Arugula", "arugula.jpg", "Like many vegetables, arugula needs regular watering for healthy growth and optimal flavor. It has a shallow root system. Keep the soil consistently moist but not soggy, watering as soon as the top inch of soil feels dry. In dry climates, this might mean watering every morning."],
    "turnip" : ["Turnip", "turnip.jpg", "Turnips will germinate best in deeply watered soil. When growing, the roots need consistent moisture. Apply 1 inch of water a week if Mother Nature hasn't done the job for you. In very sandy, fast-draining soil, apply up to 2 inches of water a week."],
    #zone 8
    "okra" : ["Okra", "okra.jpg", "Young plum trees need to be watered at least once a week to promote healthy root growth. Once the tree is established, it requires regular watering, especially in the dry summer months. Deeply water your plum tree once every two to four weeks."],
    #zone 9
    "broccoli" : ["Broccoli", "broccoli.jpeg", "Broccoli requires proper irrigation to achieve optimum growth. Water plants daily for the first week to get the crop established. Continue to irrigate broccoli every four to five days, as needed, to keep the plants healthy."],
    "brusselSprout": ["Brussel Sprouts", "brusselSprout.jpg", "Water Brussels sprouts deeply and infrequently while trying to maintain even soil moisture. About 1-2 inches of water are required per week. Use drip irrigation if possible to conserve water. Applying mulch around the plant also helps conserve soil moisture and reduce weed growth. Moisture fluctuations during heading will cause maturing sprouts to split open or develop bitter flavors."],
    "cabbage":['Cabbage', 'cabbage.jpg', "Water your cabbage once a week, applying 1 1/2 inches of water to the soil. If the soil is dry to a depth of 3 inches, water more frequently. Water in the morning to avoid water sitting on the plant's leaves, which encourages pests and diseases."],
    "okra": ['Okra', 'okra.jpg', "Okra is appreciated for its ability to withstand drought compared to other vegetables, but for good growth and production, you'll need to water at least an inch a week, just as with other vegetables."],
    "spinach": ['Spinach', 'spinach.jpg', "Spinach needs about one to one and a half inches of rain or irrigation per week. If you do not get any rain, you will need to manually water your spinach plants. Instead of one long deep soak, spinach plants will do better with three or four light waterings per week."],
    #zone 10
    "radish": ['radish', 'radish.jpg', 'If the planting does not get one inch of rain each week, soak the soil thoroughly at least once a week.'],
    "bitterMelon": ['Bitter Melon', 'bitterMelon.jpg', 'Bitter melon likes a lot of water and humidity. Keep its soil moist throughout the growing season, checking it more often in hot weather. Water twice a week or whenever the surface soil dries out.'],
    "jicama": ['Jicama', 'jicama.jpg', 'Jicama does not tolerate soggy soil, but it does require consistent waterings that prevent the soil from drying out. Water the plant at the soil line rather than on the leaves. Ensure your jicama plants receive at least 2 inches of water per week to mature and produce healthy tubers.'],
    "peanut": ['Peanut', 'peanut.jpeg', 'Depending on region and climate, peanuts typically require between 20 to 28 inches of water through- out the growing season'],
    "tomatillo": ['Tomatillos', 'tomatillo.png', 'Tomatillos are fairly drought-tolerant but thrive best with about 1 inch of water per week.'],
    #zone 11
    "beet": ['Beets', 'beet.jpg', 'A good watering schedule for beets provides an inch of water per week.'],
    "carrot": ['Carrots', 'carrot.jpg', 'Carrots need at least 1 inch of water each week during the growing season from rainfall or irrigation. Always soak the soil thoroughly when watering.'],
    "kale":  ['Kale', 'kale.jpg', 'Kale needs consistent amount of water to stay healthy, generally growing best in 1 to 1 1/2 inches of water per week.'],
    "sweetPea": ['Sweet Peas', 'sweetPea.jpg', 'Plants need about 1 inch of rain per week during the growing season. Keep the soil moist but not saturated.'],
    "swissChard": ['Swiss Chard', 'swissChard.jpg', "Swiss chard does best with a nice, even supply of water. Water regularly, applying 1 to 1.5 inches of water per week if it doesn't rain."],
    #zone 12 incomplete need picss
    "bushBean": ['Bush Beans', 'bushBean.jpg', 'Water regularly, about 2 inches per square foot per week. If you do not keep beans well watered, they will stop flowering.'],
    "eggplant": ['Eggplant', 'eggplant.jpg', 'Water eggplant deeply and infrequently, applying 1-2 inches per week. Use drip irrigation if possible. Mulching around the plant will conserve soil moisture and reduce weed growth. Irrigate so that moisture goes deeply into the soil.'],
    "hotPepper": ['Hot Peppers', 'hotPepper.jpg', 'Deeply water the plants with 1 inch of water per week, and adjust the amount or frequency during hot, dry periods, after rainfall or if your soil is sandy and drains fast.'],
    "summerSquash": ['Summer Squash', 'summerSquash.jpg', 'Squash plants require an inch of water a week, or up to two inches during the hottest stretch of summer.'],
    "tomato": ['Tomato', 'tomato.jpg', 'Garden tomatoes typically require 1-2 inches of water a week. Tomato plants grown in containers need more water than garden tomatoes.'],
}

#fruDict: contain all fruits, based on name input info onto template 
#dictionary of lists with following information [title name, image, water description]
fruitDict = {
    #zone 1
    "tomato": ['Tomato', 'tomato.jpg', 'Garden tomatoes typically require 1-2 inches of water a week. Tomato plants grown in containers need more water than garden tomatoes.'],
    "chokecherry" : ["Chokecherry", "chokecherry.jpeg", "A newly planted Common chokecherry tree will need consistently moist soil for its first year or two. After establishment, these trees are extremely drought tolerant and will only need watering during dry spells. Avoid watering the canopy of the tree and supply it with water at the base of its trunk."],
    "haskap" : ["Haskap", "haskap.jpeg", "Depending on the soil type, deep water the plant every 5 to 7 days. Frequent, shallow watering events discourage deep root development."],
    'sepRubyApple' : ['September Ruby Apple', 'sepRubyApple.jpeg', "Give your apple tree enough water to soak the ground all around the roots."],
    #zone 2
    "brookgoldPlum" : ["Brookgold Plums", "brookgoldPlum.jpg", "It does best in average to evenly moist conditions, but will not tolerate standing water. It is not particular as to soil type or pH."],
    "koreanPine" : ["Korean Pine", "koreanPine.jpeg", "Water when normal rainfall does not provide the preferred 1 inch of moisture most plants prefer. Average water is needed during the growing season, but take care not to overwater. The first two years after a plant is installed, regular watering is important. The first year is critical. It is better to water once a week and water deeply, than to water frequently for a few minutes."],
    "norkentApple" : ["Norkent Apple", "norkentApple.jpeg", "apple trees need about an inch of rainfall every seven to ten days for established trees. Another way of looking at it is water when the top eight to ten inches of soil are dry."],
    #zone 3
    "cupidCherry" : ["Cupid cherry", "cupidCherry.jpeg", "After planting, watering cherry trees properly their first year is extremely important. They should be watered the first week every other day, deeply; the second week they can be watered deeply two to three times; and after the second week, water cherry trees thoroughly once a week for the rest of the first season."],
    "dolgoCrabapple" : ["Dolgo Crabapple", "dolgoCrabapple.jpeg", "During its first year of growth, crabapple trees need regular watering. Keep the soil evenly moist over the root zone, about an inch per week. Once it is well established, crabapples are very drought tolerant and shouldn't need supplemental watering unless the season is extremely dry"],
    "goldSpicePear" : ["Golden Spice Pear", "goldSpicePear.jpeg", "Water when normal rainfall does not provide the preferred 1 inch of moisture most plants prefer. Average water is needed during the growing season, but take care not to overwater. The first two years after a plant is installed, regular watering is important. The first year is critical. It is better to water once a week and water deeply, than to water frequently for a few minutes."],
    #zone 4
    'buartnut' : ["Buartnut", "buartnut.jpeg", "Buartnut tree care requires irrigation. Water the seedling well and regularly for the first year or two of its life in your backyard."],
    'ewingBluePlum' : ["Ewing Blue Plum", "ewingBluePlum.jpeg", "Once every 10 days or two weeks is plenty. Worse than dry, thirsty roots is waterlogged, drowning roots."],
    'novaPear' : ["Nova Pear", "novaPear.jpeg", "Average water is needed during the growing season, but take care not to overwater. The first two years after a plant is installed, regular watering is important. The first year is critical. It is better to water once a week and water deeply, than to water frequently for a few minutes."],

    #zone 5
    
    #zone 6
    "lateCrawford" : ["Late Crawford Peaches", "latecrawfordpeaches.jpg", "Peach trees require regular watering for an average of three times per week as the young tree gets established. As time goes on and the tree takes hold in the ground, the young tree should be watered-in well on a less frequent basis, soaking the soil generously only when the soil is relatively dry."],
    #zone 7
    "ozarkPlum" : ["Ozark Plum", "ozarkplum.jpg", "Young plum trees need to be watered at least once a week to promote healthy root growth. Once the tree is established, it requires regular watering, especially in the dry summer months. Deeply water your plum tree once every two to four weeks."],
    "turkeyFig" : ["Turkey Fig", "turkeyFig.jpg", "The Brown Turkey fig tree requires two waterings per week for the first three months after it's planted. Mature trees require one to 1.5 inches of water per week."],
    #zone 8
    "montmorencyCherry" : ["Montmorency Cherry", "montmorency.jpg", "Cherry Trees enjoy moist soil. They need an inch of water every two weeks while they're young. It may be a good idea to keep up with the rainfall with weather reports, or a rain gauge to see how much rainwater your trees are getting. During times of drought, your trees may need a little extra water."],
    "washngtonOrange" : ["Washington Orange", "washingtonorange.jpg", "A young orange tree should be watered every few days, but a more mature tree can be watered anywhere from weekly to about once a month. If it's during the dry season, you should water your orange tree every few days or when the soil has dried up. During the rainy season, you may not need to water your orange tree."],
    #zone 9
    "avocado": ['Avocado', 'avocado.jpg', 'Most avocado roots stay in the top six inches of soil, which can dry out quickly. Newly planted trees may need water two to three times per week their first year. Mature avocado trees need water equal to about 2 inches of rainfall or irrigation each week during summer.'],
    "hardyKiwi": ['Hardy Kiwi', 'hardyKiwi.jpg', 'Hardy kiwi relies on at least one inch of rainfall every 10 days, especially right after planting.'],
    "olive": ['Olives', 'olive.jpg', 'Water an establishing olive tree once weekly for the first year or anytime the top 2??? of soil becomes dry. After an olive tree is established, deep watering once monthly is sufficient.'],
    "passionFruit": ['Passionfruit', 'passionfruit.jpg', 'Keep the soil evenly moist for quick, even growth. Keep the soil moist but not wet. Plant in moisture-retentive, well-drained soil.'],
    "starFruit": ['Starfruit', 'starfruit.jpg', 'Water your starfruit tree regularly, 2-3 times per week if no rain. Starfruit trees are not tolerant of drought.'],
    #zone 10
    "appleGuava": ['Apple Guava', 'appleGuava.jpg', 'Water 2 - 3 times per week until established.'],
    "caricaPapaya": ['Carica Papaya', 'caricaPapaya.jpg', 'Papayas need plenty of water to grow tasty fruit, but the plants do not tolerate wet feet.To avoid overwatering the papaya, water deeply only when the top 1 inch of soil dries.'],
    "jackFruit": ['Jackfruit', 'jackfruit.jpg', 'Water your jackfruit tree every day, but be careful not to over-water. Young jackfruit trees need water every day so that their roots can establish. You can use a garden hose or a watering can to water the tree at its base. In order to avoid overwatering, make sure the soil is damp 1.5 inches (3.8cm) deep, but no more.'],
    "junePlum": ['June Plum', 'junePlum.jpg', 'When watering June Plum Trees make sure to lightly soak the soil and then do not water again until the top 2 inches are dry.'],
    "soursop": ['Soursop', 'soursop.jpg', "Water regularly, but do not allow the soil to become soaking. Ensure it drains away well."],
    #zone 11 
    "jaboticaba": ['Jaboticaba', 'jaboticaba.jpg', 'Water should be supplied as needed to maintain good soil moisture and prevent wilting, but constant flooding is undesirable. As the root system is somewhat shallow, irrigation is usually required when the upper inch or two of soil become dry.'],
    "macadamia": ['Macadamia', 'macadamia.jpg', 'Water freshly sown plants deeply, tamping down the soil a second time to remove any remaining air pockets, and maintain evenly moist soil until your plant begins to grow. Then, in the absence of a drenching rain, water weekly year-round.'],
    "mango": ['Mango', 'mango.jpg', 'No matter what age the mango tree is, the amount of water stays the same: 1 inch (2.5 cm) of water over the course of the week.'],
    "natalPlum": ['Natal Plum', 'natalPlum.jpg', 'The Natal plum requires moderate watering conditions.  Be sure not to overwater because it is susceptible to root rot.'],
    "seaGrape": ['Sea Grape', 'seaGrape.jpg', 'The sea grape is drought-tolerant, but should be watered if grown in a container; once transferred to the ground, watering is not necessary as long as you live in a tropical area with lots of rainfall, but regular watering can help it grow fuller.'],
    #zone 12
    "africanApricot": ['African Apricot', 'africanApricot.jpg', 'Your apricot tree needs regular watering at one inch per week. The top 8 to 10 inches of soil should remain moist throughout the growth period.'],
    "ackee": ['Ackee', 'ackee.jpg', 'Newly planted ackee trees should be watered at planting and every other day for the first week or so and then 1 to 2 times a week for the first couple of months.'],
    "bignay": ['Bignay', 'bignay.jpg', 'Once well established, bignay trees seem to be quite drought tolerant and can go for several weeks without irrigation during our spring dry season. They prefer though, to have a good watering about once a week for good growth and fruit development.'],
    "imbe": ['Imbe', 'imbe.jpg', 'You should water the Philodendron Imbe so that the soil remains moist without any excess water.'],
    "blackPepper": ['Black Pepper', 'blackPepper.jpg', 'Black pepper plants need damp soil and grow best when watered several times a week. In hotter climates, you may need to water your plant more often. Stick a finger in the soil to check its moisture level; if the soil feels dry or hot, water your plant.'],


}

@app.route('/Vegetable/<veg>')
def vegTemp(veg):
    return render_template('vegetables/vegTemp.html', veg = veg, vegDict = vegDict)

@app.route('/Fruit/<fru>')
def fruTemp(fru):
    return render_template('fruits/fruTemp.html', fru = fru, fruitDict = fruitDict)

@app.route('/')
def home():
    return render_template('my_template.html')

@app.route('/regions', methods=['GET'])
def regions():
    return render_template('regions.html')

### ZONES BELOW ###
@app.route('/zone1', methods=['GET'])
def zone1():
    return render_template('zone1.html')

@app.route('/zone2', methods=['GET'])
def zone2():
    return render_template('zone2.html')

@app.route('/zone3', methods=['GET'])
def zone3():
    return render_template('zone3.html')

@app.route('/zone4', methods=['GET'])
def zone4():
    return render_template('zone4.html')

@app.route('/zone5', methods=['GET'])
def zone5():
    return render_template('zone5.html')

@app.route('/zone6', methods=['GET'])
def zone6():
    return render_template('zone6.html')

@app.route('/zone7', methods=['GET'])
def zone7():
    return render_template('zone7.html')

@app.route('/zone8', methods=['GET'])
def zone8():
    return render_template('zone8.html')

@app.route('/zone9', methods=['GET'])
def zone9():
    return render_template('zone9.html')

@app.route('/zone10', methods=['GET'])
def zone10():
    return render_template('zone10.html')

@app.route('/zone11', methods=['GET'])
def zone11():
    return render_template('zone11.html')

@app.route('/zone12', methods=['GET'])
def zone12():
    return render_template('zone12.html')
### END OF ZONES ###

import pickle as p
with open('accessories.dat','wb') as f1:
    txt='''Sunglasses
Apron
Necklace
Watch
Socks
Tie
Bow tie
Purse
Ring
Gloves
Scarf
Umbrella
Boots
Mittens
Stockings
Earmuffs
Hairclip
Bobbypin
Hairband
Safetypin
Pocketwatch'''
    t=txt.split()
    p.dump(t,f1)
with open('foods.dat','wb') as f2:
    txt1='''Icaco
Ice
Ice Cream
IcebergLettuce
Idli
Ikizukuri
Inarizushi
Injera
Isaw
Ital
ItalianSausage
Ham
Hamburger
HashBrowns
Herring
HoisinSauce
Honey
Honeydew
Horseradish
HotDogs
HotSauce
Huckleberries
Hummus
Anchovies
Asparagus
Avocados
Alfredosauce
Arugula
Almonds
Amaranth
Apples
Bacon
Bagels
Bananas
Barbecue
Barley
Basil
Beans
Beef
Beets
Blackberries
Blueberries
Bread
Broccoli
Burgers
Cabbage
Cake
Calzones
Cheese
Chicken
Chili
Coconut
Cod
Coffee
Collards
Cookies
Crepes
Curry'''

    t1=txt1.split()
    p.dump(t1,f2)

    

    
    

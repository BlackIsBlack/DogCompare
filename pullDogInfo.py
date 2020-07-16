from re import findall

dogHTML = open('dogBreeds.html', 'r').read()

dogNames = findall('<b>Web Source Name:</b>&nbsp;[^A-Z]+([^\&]+)',dogHTML)
dogImages = findall('breed_image_thumb/([^\.]+).jpg',dogHTML)

for image in range(len(dogImages)):
    dogImages[image] = f'https://bigd.big.ac.cn/idog/images/breed_image_thumb/{dogImages[image]}.jpg'
writing = ""
for i in range(len(dogNames)):
    try:
        writing += f'{dogNames[i]},{dogImages[i]}\n'
    except:
        writing += f'{dogNames[i]},No Image\n'
outputFile = open('dogInfo.csv','w')
outputFile.write(writing)
outputFile.close()

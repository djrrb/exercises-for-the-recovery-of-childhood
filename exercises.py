#coding:utf-8

myFontSize = 80*.90
myLineHeight = 110*.95
myFont = 'RoslindaleText-Regular'
m = 240

textColor = (1, 1, 1)
bgColor = (0, 0, 0)
captionColor = (1, 1, 1, .7)

with open('/Users/david/Documents/Clients/exercises-for-the-recovery-of-childhood/Exercises for the Recovery of Childhood.txt', 'r', encoding="utf-8") as textFile:
    text = textFile.read()
    stories = text.split('\n\n')
    

    
    for i, story in enumerate(stories[2:]):
        
        newPage(2048, 2700)
        
        #hyphenation(True)
        
        fill(*bgColor)
        rect(0, 0, width(), height())
        fill(*textColor)
        lines = story.split('\n')
        
        storyText = '\n'.join(lines[:-1])
        sentences = storyText.split('. ')
        
        fs = FormattedString('', 
        fontSize=myFontSize, 
        lineHeight=myLineHeight, 
        font=myFont, 
        fill=textColor
        )
        
        for si, sentence in enumerate(sentences):
            if si == 0:
                myFont = 'RoslindaleText-Bold'
            else:
                myFont= 'RoslindaleText-Regular'
            if si != len(sentences) - 1:
                sentence = sentence + '. '
            fs.append(sentence, 
            font=myFont, )
        
        

        
        overflow = textBox(fs, (m, m, width()-m*2+50, height()-m*2))
        if overflow:
            print(i)
            
        
            
        subhead = 'Exercises on the Recovery of Childhood, '+ str(i+1) + '/62'
        fs = FormattedString(subhead.upper(), fontSize=myFontSize*.70, lineHeight=myFontSize*1, font='OutputSans-Bold', tracking=3, fill=captionColor)

            
        textBox(fs, (m, m-150, width()-m*2, 200))
            
        saveImage('proofs/story'+str(i)+'.png')
saveImage('proofs/stories.pdf')

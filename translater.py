from translate import Translator

language={'Hindi':'hi','Chinese':'zh','Spanish':'es',
          'German':'de','French':'fr','Arabic':'ar',
          'Russian':'ru','Portuguese':'pt'
          }
print('following are language for translation')
for index,key in enumerate(language,start=1):
    print(f'{index}.{key}')
try:
    user_choose=int(input('enter your choose'))
    print(user_choose)
    language_list = list(language.keys())
    selected_language=language_list[user_choose-1]
    code=language[selected_language]
    print('selected language', selected_language)
    print('language code',code)

    translator =Translator(to_lang=code)
    user_text=input('enter text you want to translat ')
    translation=translator.translate(user_text)
    print(translation)
    
except Exception as e:
    print('some error come ',e)




# image_file=['image.jpg','image2.jpg','image3.jpg','image4.jpg','image5.jpg']
# pdf_file=input('enter.pdf name')
# doc=SimpleDocTemplate(pdf_file,pagesize=A4)
# elements=[]
# for img in image_file:
#     im=Image(img,width=450,height=400)
#     elements.append(im)
#     elements.append(Spacer(1,3))
# doc.build(elements)

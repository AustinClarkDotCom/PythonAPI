    #Imports#
import os
from openai import OpenAI
from dotenv import load_dotenv


    #API Key#
load_dotenv()
API_KEY =  os.getenv('api_key')

client = OpenAI(
  api_key=API_KEY,
  organization='org-W8WGu4kNhNyPuWV7ICbwmBzO',
)

    #Emotions#
isEmotionEntry = False
Emotion = "Neutral"
def Emotions():
  Emotion = input('DUNGEON MASTER: \nHow is this character feeling?: \n1) Angry\n2) Sad\n3) Happy\n4) Anxious\n5) Factual\n Enter Emotion: ')
  EmotionList = ('Angry', 'Happy', 'Sad', 'Anxious', 'Factual')
  for i in EmotionList:
      if Emotion == i:
        isEmotionEntry = True
        return isEmotionEntry, Emotion
        break


    #Characters#
isCharacterEntry = False
def Characters():
  Character = input("\nDUNGEON MASTER: \nWho is the character the party is speaking to? \n1) Orc\n2) Elf\n3) Dwarf\n Enter Character: ")
  CharChoice = {
  "Orc": "Orc, who speaks in very simple terms",
  "Elf": "Elf, Who Speaks very intelligently",
  "Dwarf": "Dwarf, who speaks rougher and more plain than most"
}
  
  for key in CharChoice:
      if Character == key:
        isCharacterEntry = True
        break
  Character = CharChoice[Character]
  return isCharacterEntry, Character
  

  #Check if entries exist to interact#
while isEmotionEntry == False:
  isEmotionEntry, Emotion = Emotions()

while isCharacterEntry == False:
  isCharacterEntry, Character = Characters()

Character = "You are a" + " " + Emotion + " " + Character

if isCharacterEntry == True:
   if isEmotionEntry == True:
      Speech_Interaction = input("\nWhat would you like to say?\nEnter Speech: ")
      completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role": "system", "content": Character},
          {"role": "user", "content": f"respond to the following as the provided fantasy character {Speech_Interaction}"}
        ]
      )
      print("")
      print(completion.choices[0].message.content)
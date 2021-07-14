import os
import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

my_secret = os.environ['TOKEN']
client = discord.Client()

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 
chromeOptions.add_argument("--remote-debugging-port=9222")
chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument("--disable-gpu") 
chromeOptions.add_argument("start-maximized") 
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument(r"user-data-dir=.\cookies\\test") 
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.pso2keeper.com/")

#Test Message
#driver = initChrome()
#testp = driver.find_element_by_class_name('font-weight-light').text
#print(testp)

@client.event
async def on_ready():
  print('Logged on as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hi'):
    await message.channel.send('hey')
  
  if message.content.startswith('$init'):
    if len(str(message.content)) == 5:
      await message.channel.send('Please specify Permission Token')
    else:
      while True:
        try:
          tExtract = str(message.content).lstrip('$init ')
          showFormB = driver.find_element_by_xpath("//button[2]")
          showFormB.click()
          listMissionB = driver.find_elements_by_class_name('v-select__selections')[0]
          listMissionB.click()
          missionSelB = driver.find_element_by_id('第6使徒殲滅作戦-list-item-73')
          missionSelB.click()
          quotaListB = driver.find_elements_by_class_name('v-select__selections')[1]
          quotaListB.click()
          quotaSelB = driver.find_element_by_id('32-list-item-84')
          quotaSelB.click()
          CPT = driver.find_element_by_id('input-67')
          CPT.send_keys(Keys.CONTROL,"a")
          CPT.send_keys(Keys.DELETE)
          CPT.send_keys(tExtract)
          submitB = driver.find_elements_by_xpath("//*[contains(text(), 'Submit')]")[0]
          submitB.click()
          gKey = driver.find_elements_by_xpath("//*[contains(text(), 'Group Key')]")[0].text
          await message.channel.send(gKey + ' ' + tExtract)
          driver.refresh()
          print("Request Finished")
        except :
          driver.refresh()
          continue
        break
  
  # if message.content.startswith('+'):
  #   if len(message.content) == 1:
  #     await message.channel.send(str(message.author) + ' joined')
  #   else:
  #     await message.channel.send(str(message.author) + ' joined as ' + str(message.content).lstrip("+ "))

  if message.content.startswith('$ref'):
    driver.refresh()
    await message.channel.send('Refresh Completed')
    print('Refresh Completed')

client.run(my_secret)

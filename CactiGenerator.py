import os
import asyncio
import time
from pyppeteer import launch
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


while True:
    # DELETE OLD IMAGES.
    if os.path.exists("ImagensCacti/BackBone1.png"):
        os.remove("ImagensCacti/BackBone1.png")
    if os.path.exists("ImagensCacti/BackBone2.png"):
        os.remove("ImagensCacti/BackBone2.png")
    if os.path.exists("ImagensCacti/Corporativos.png"):
        os.remove("ImagensCacti/Corporativos.png")
    if os.path.exists("ImagensCacti/Temperaturas.png"):
        os.remove("ImagensCacti/Temperaturas.png")
    print("CactiBot: Todas as atualizações antigas foram apagadas!")
    # DELETE OLD IMAGES.

    # MAIN FUNCTION
    async def main():
        browser = await launch()
        page = await browser.newPage()

        # FONTE BACKBONE IPATINGA
        await page.setViewport({'width': 1120, 'height': 720})
        print('CactiBot: Gerando o BACKBONE DE IPATINGA...')
        await page.goto(
            '') # LINK DEVE FICAR ENTRE ASPAS
        await page.keyboard.sendCharacter('') # USUARIO ENTRE AS ASPAS
        await page.mouse.click(666, 197)
        await page.keyboard.sendCharacter('') # SENHA ENTRE AS ASPAS
        await page.keyboard.press('Enter')
        await asyncio.sleep(5.0)
        await page.screenshot({'path': 'ImagensCacti/BackBone1.png', 'fullpage': True})
        print('CactiBot: BACKBONE DE IPATINGA Gerado com sucesso!')
        # FONTE BACKBONE IPATINGA

        # FONTE BACKBONE VALADARES
        await page.setViewport({'width': 1280, 'height': 720})
        print('CactiBot: Gerando o BACKBONE DE VALADARES...')
        await page.goto(
            '') # LINK DEVE FICAR ENTRE AS ASPAS
        await page.keyboard.sendCharacter('') # USUARIO ENTRE AS ASPAS
        await page.mouse.click(666, 197)
        await page.keyboard.sendCharacter('') # SENHA ENTRE AS ASPAS
        await page.keyboard.press('Enter')
        await asyncio.sleep(5.0)
        await page.screenshot({'path': 'ImagensCacti/BackBone2.png', 'fullpage': True})
        print('CactiBot: BACKBONE DE VALADARES Gerado com sucesso!')
        # FONTE BACKBONE VALADARES

        # FONTE CORPORATIVOS
        await page.setViewport({'width': 1280, 'height': 720})
        print('CactiBot: Gerando os CORPORATIVOS...')
        await page.authenticate({'username': '', 'password': ''}) # USERNAME E PASSWORD ENTRE AS ASPAS
        await page.goto('') # LINK ENTRE AS ASPAS
        await page.screenshot({'path': 'ImagensCacti/Corporativos.png', 'fullpage': True})
        print('CactiBot: CORPORATIVOS Gerados com sucesso!')
        # FONTE CORPORATIVOS

        # FONTE TEMPERATURAS
        await page.setViewport({'width': 1880, 'height': 1200})
        print('CactiBot: Gerando as TEMPERATURAS...')
        await page.goto('') # LINK ENTRE AS ASPAS
        await page.keyboard.sendCharacter('') # USUARIO ENTRE AS ASPAS
        await page.keyboard.press('Enter')
        await page.keyboard.sendCharacter('') # SENHA ENTRE AS ASPAS
        await page.keyboard.press('Enter')
        await asyncio.sleep(10.0)
        await page.screenshot({'path': 'ImagensCacti/Temperaturas.png', 'fullpage': True})
        print('CactiBot: TEMPERATURAS Geradas com sucesso!')
        # FONTE TEMPERATURAS

        await browser.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # MAIN FUNCTION
    print("CactiBot: Programa parado, Aguardando o tempo de execução.")
    time.sleep(300)


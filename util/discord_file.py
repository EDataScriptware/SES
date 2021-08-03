from discord_webhook import DiscordWebhook

WEBHOOK_URL = "https://discord.com/api/webhooks/872195980425064458/hH3OxjytbYxIlV-oOiEX7eBujtppzBh_Tv6mrIO7jXL2tr-ei4-3--5RnVuLW2riYB2t"

def send_message(message):
    webhook = DiscordWebhook(url=WEBHOOK_URL, content=str(message))
    response = webhook.execute()
    print(response)

def logged_on(name, game):
    message = name + " has logged onto " + game + "!" 
    webhook = DiscordWebhook(url=WEBHOOK_URL, content=str(message))
    response = webhook.execute()
    print(response)

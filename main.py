import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(user_agent='ai-bot (ai-bot@ai-bot.xyz)', language='ja')
page_py = wiki_wiki.page('カンニング')
if page_py.exists():
    print(page_py.text)
else:
    print("ページが存在しません")
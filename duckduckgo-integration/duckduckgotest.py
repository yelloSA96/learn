from duckduckgo_search import DDGS

results = DDGS().text("gundam", max_results=5)
print(results)
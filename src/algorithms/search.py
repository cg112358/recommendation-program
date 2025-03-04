def search_recommendations(data, query):
    results = {}
    for category, items in data["recommendations"].items():
        if query in category:
            # Sort items by rating in descending order
            sorted_items = sorted(items, key=lambda x: x.get("rating", 0), reverse=True)
            results[category] = sorted_items
    return results
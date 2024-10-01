def run():
    # Шаг 1: Ввод магазинов
    stores = {}
    store_names = input("Введите названия магазинов через запятую: ").split(",")
    for store_name in store_names:
        store_name = store_name.strip()
        if store_name:
            stores[store_name] = {}

    # Шаг 2: Ввод товаров
    products = []
    product_names = input("Введите названия товаров через запятую: ")
    for product_name in product_names.split(","):
        product_name = product_name.strip()
        if product_name and product_name not in products:
            products.append(product_name)

    # Шаг 3: Ввод цен товара в магазинах
    prices = {}
    for product in products:
        price_input = input(
            f"Введите цены товара '{product}' в магазинах ({', '.join(stores.keys())}) через запятую: ")
        prices[product] = list(map(float, price_input.split(",")))

    # Шаг 4: Вычисление общей стоимости в каждом магазине
    total_costs = {store: 0 for store in stores}
    for product, price_list in prices.items():
        for store, price in zip(stores.keys(), price_list):
            total_costs[store] += price

    print("\nСписок магазинов и общая стоимость покупок:")
    for store, total in total_costs.items():
        print(f" - В магазине '{store}' общая стоимость: {total:.2f} рублей")

    cheapest_store = min(total_costs, key=total_costs.get)
    print(f"\nВы можете сэкономить больше всего в магазине '{cheapest_store}'.")

if __name__ == "__main__":
    run()
class OrderProcessor:
    def process_order(self, order):
        # Step 1: Validate order details
        self.ValidateOrder(order)

        # Step 2: Calculate total price
        totalPrice = self.CalculatePrice(order)

        # Step 3: Apply discounts if applicable
        totalPrice = self.ApplyDiscount(order, totalPrice)

        # Step 4: Update inventory
        self.UpdateInventory(order)

        # Step 5: Generate receipt
        receipt = self.GenerateReceipt(order, totalPrice)

        # Step 6: Send confirmation email
        self.SendEmail(order, receipt)

        return receipt
    
    def ValidateOrder(self, order):
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")
    
    def CalculatePrice(self, order):
        totalPrice = 0
        for item in order["items"]:
            totalPrice += item["price"] * item["quantity"]
        return totalPrice

    def ApplyDiscount(self, order, totalPrice):
        if order.get("discount_code") == "SUMMER20":
            totalPrice *= 0.8  # 20% discount
        elif order.get("discount_code") == "WELCOME10":
            totalPrice *= 0.9  # 10% discount
        return totalPrice

    def UpdateInventory(self, order):
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    def GenerateReceipt(self, order, totalPrice): 
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${totalPrice:.2f}\n"

        return receipt

    def SendEmail(self, order, receipt): 
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")
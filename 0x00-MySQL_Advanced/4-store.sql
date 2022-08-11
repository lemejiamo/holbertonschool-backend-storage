-- SQL script that creates a trigger thar
-- decreases the quantity of an item after adding a new order.
CREATE TRIGGER items_ai AFTER INSERT ON orders FOR EACH ROW
UPDATE items set quantity=quantity-NEW.number
WHERE items.name = NEW.item_name;

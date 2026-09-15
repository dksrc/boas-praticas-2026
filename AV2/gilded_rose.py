class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def att(self):
        for x in range(len(self.items)):
            if self.items[x].name != "Aged Brie" and self.items[x].name != "Backstage passes to a TAFKAL80ETC concert":
                if self.items[x].quality > 0:
                    if self.items[x].name != "Sulfuras, Hand of Ragnaros":
                        self.items[x].quality = self.items[x].quality - 1
            else:
                if self.items[x].quality < 50:
                    self.items[x].quality = self.items[x].quality + 1
                    if self.items[x].name == "Backstage passes to a TAFKAL80ETC concert":
                        if self.items[x].sell_in < 11:
                            if self.items[x].quality < 50:
                                self.items[x].quality = self.items[x].quality + 1
                        if self.items[x].sell_in < 6:
                            if self.items[x].quality < 50:
                                self.items[x].quality = self.items[x].quality + 1
            if self.items[x].name != "Sulfuras, Hand of Ragnaros":
                self.items[x].sell_in = self.items[x].sell_in - 1
            if self.items[x].sell_in < 0:
                if self.items[x].name != "Aged Brie":
                    if self.items[x].name != "Backstage passes to a TAFKAL80ETC concert":
                        if self.items[x].quality > 0:
                            if self.items[x].name != "Sulfuras, Hand of Ragnaros":
                                self.items[x].quality = self.items[x].quality - 1
                    else:
                        self.items[x].quality = self.items[x].quality - self.items[x].quality
                else:
                    if self.items[x].quality < 50:
                        self.items[x].quality = self.items[x].quality + 1

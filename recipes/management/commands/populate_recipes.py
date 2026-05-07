import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from recipes.models import Recipe


SAMPLE_RECIPES = [
    {
        "title": "Classic Spaghetti Bolognese",
        "description": "A rich, hearty Italian meat sauce slow-cooked to perfection and served over al-dente spaghetti. A timeless family favourite.",
        "ingredients": "400g spaghetti\n500g minced beef\n1 large onion, finely chopped\n3 garlic cloves, minced\n2 cans (400g each) crushed tomatoes\n2 tbsp tomato paste\n1 tsp dried oregano\n1 tsp dried basil\n1 carrot, finely grated\n2 tbsp olive oil\nSalt and black pepper to taste\nParmesan cheese for serving",
        "instructions": "Heat olive oil in a large pan over medium heat.\nAdd onion and carrot, cook for 5 minutes until softened.\nAdd garlic and cook for 1 more minute.\nAdd minced beef and brown thoroughly, breaking up lumps.\nStir in tomato paste and cook for 2 minutes.\nAdd crushed tomatoes, oregano, basil, salt, and pepper.\nSimmer on low heat for 30–40 minutes, stirring occasionally.\nCook spaghetti according to package instructions.\nDrain pasta and toss with the Bolognese sauce.\nServe topped with grated Parmesan cheese.",
        "cooking_time": 50,
    },
    {
        "title": "Creamy Chicken Tikka Masala",
        "description": "Tender chicken pieces marinated in spiced yoghurt, grilled, then simmered in a luscious tomato-cream sauce. Restaurant quality at home!",
        "ingredients": "700g chicken breast, cubed\n1 cup plain yoghurt\n2 tsp garam masala\n1 tsp turmeric\n1 tsp cumin\n1 tsp chilli powder\n3 tbsp butter\n1 large onion, diced\n4 garlic cloves, minced\n1 tbsp fresh ginger, grated\n1 can (400g) crushed tomatoes\n1 cup heavy cream\nFresh coriander for garnish\nSalt to taste",
        "instructions": "Mix yoghurt, garam masala, turmeric, cumin, chilli powder, and salt in a bowl.\nAdd chicken, coat well, and marinate for at least 30 minutes (overnight is better).\nGrill or pan-fry the marinated chicken until charred and cooked through. Set aside.\nMelt butter in a large pan. Add onion and cook until golden.\nAdd garlic and ginger, cook for 2 minutes.\nAdd crushed tomatoes and remaining spices. Simmer for 10 minutes.\nBlend the sauce until smooth using an immersion blender.\nAdd cream and cooked chicken. Simmer for 10 minutes.\nGarnish with fresh coriander and serve with naan or rice.",
        "cooking_time": 45,
    },
    {
        "title": "Fluffy Buttermilk Pancakes",
        "description": "Light, tall, and perfectly golden pancakes made with buttermilk for extra tenderness. The ultimate weekend breakfast treat.",
        "ingredients": "2 cups all-purpose flour\n2 tbsp sugar\n2 tsp baking powder\n1/2 tsp baking soda\n1/2 tsp salt\n2 cups buttermilk\n2 large eggs\n4 tbsp melted butter\n1 tsp vanilla extract\nButter and maple syrup to serve",
        "instructions": "Whisk flour, sugar, baking powder, baking soda, and salt in a large bowl.\nIn another bowl, whisk buttermilk, eggs, melted butter, and vanilla.\nPour wet ingredients into dry ingredients and stir gently until just combined (lumps are fine).\nLet batter rest for 5 minutes.\nHeat a non-stick pan over medium heat and lightly grease with butter.\nPour 1/4 cup batter per pancake. Cook until bubbles form on top.\nFlip and cook for 1–2 minutes until golden.\nServe warm with butter and maple syrup.",
        "cooking_time": 25,
    },
    {
        "title": "Avocado Toast with Poached Eggs",
        "description": "A nutritious and trendy breakfast featuring creamy smashed avocado on toasted sourdough, topped with perfectly poached eggs.",
        "ingredients": "2 thick slices sourdough bread\n2 ripe avocados\nJuice of 1 lemon\nSalt and cracked black pepper\n1/4 tsp chilli flakes\n4 large eggs\n1 tbsp white wine vinegar\nFresh herbs (chives or parsley) for garnish\nExtra virgin olive oil",
        "instructions": "Toast the sourdough slices until golden and crispy.\nHalve and pit the avocados, scoop flesh into a bowl.\nMash avocado with lemon juice, salt, pepper, and chilli flakes.\nBring a deep saucepan of water to a gentle simmer. Add vinegar.\nCrack each egg into a small cup.\nCreate a gentle whirlpool in the water, slide eggs in one by one.\nPoach for 3–4 minutes for runny yolks.\nSpread avocado mixture generously on toast.\nTop each toast with 2 poached eggs.\nDrizzle with olive oil, garnish with fresh herbs, and serve immediately.",
        "cooking_time": 20,
    },
    {
        "title": "Homemade Margherita Pizza",
        "description": "A classic Neapolitan pizza with a thin, chewy crust, tangy tomato sauce, fresh mozzarella, and fragrant basil. Simple perfection.",
        "ingredients": "For the dough: 2.5 cups bread flour, 1 tsp instant yeast, 1 tsp salt, 1 tsp sugar, 3/4 cup warm water, 1 tbsp olive oil\nFor the topping: 1 can (400g) crushed tomatoes, 2 garlic cloves (minced), 1 tsp oregano, Salt to taste, 250g fresh mozzarella (sliced), Fresh basil leaves, Extra virgin olive oil",
        "instructions": "Mix flour, yeast, salt, and sugar in a bowl. Add warm water and olive oil.\nKnead for 8–10 minutes until smooth and elastic.\nCover and let rise in a warm place for 1 hour until doubled.\nPreheat oven to 250°C (or as high as it goes). Place a baking tray inside to heat.\nMix crushed tomatoes, garlic, oregano, and salt for the sauce.\nStretch dough on a lightly floured surface into a thin round.\nSpread sauce over dough, leaving a border for the crust.\nArrange mozzarella slices on top.\nSlide pizza onto the hot tray and bake for 10–12 minutes until crust is golden.\nRemove from oven, top with fresh basil, and drizzle with olive oil.",
        "cooking_time": 30,
    },
    {
        "title": "Chocolate Lava Cake",
        "description": "Decadent individual chocolate cakes with a warm, gooey molten centre. An impressive dessert that takes only 20 minutes to make.",
        "ingredients": "115g dark chocolate (70% cocoa)\n115g butter\n2 whole eggs\n2 egg yolks\n70g caster sugar\n2 tbsp all-purpose flour\nPinch of salt\nButter and cocoa powder for ramekins\nVanilla ice cream to serve",
        "instructions": "Preheat oven to 200°C. Butter 4 ramekins and dust with cocoa powder.\nMelt chocolate and butter together in a heatproof bowl over simmering water. Stir until smooth. Cool slightly.\nWhisk eggs, egg yolks, and sugar in a bowl until pale and thick.\nFold melted chocolate mixture into the egg mixture.\nSift in flour and salt, fold gently until just combined.\nDivide batter evenly among the 4 ramekins.\nBake for 12–13 minutes until the edges are set but centre still jiggles.\nRest for 1 minute, then run a knife around edges and invert onto plates.\nServe immediately with a scoop of vanilla ice cream.",
        "cooking_time": 20,
    },
]


class Command(BaseCommand):
    help = "Populate the database with sample recipes and a demo user."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING("Creating sample data..."))

        # Create demo user
        username = "chef_demo"
        password = "RecipeShare2024!"

        if User.objects.filter(username=username).exists():
            demo_user = User.objects.get(username=username)
            self.stdout.write(f"  [OK] Demo user '{username}' already exists.")
        else:
            demo_user = User.objects.create_user(
                username=username,
                email="chef@recipeshare.com",
                password=password,
                first_name="Chef",
                last_name="Demo",
            )
            self.stdout.write(self.style.SUCCESS(f"  [CREATED] Demo user: '{username}'"))

        # Create recipes
        created = 0
        for data in SAMPLE_RECIPES:
            recipe, was_created = Recipe.objects.get_or_create(
                title=data["title"],
                author=demo_user,
                defaults={
                    "description": data["description"],
                    "ingredients": data["ingredients"],
                    "instructions": data["instructions"],
                    "cooking_time": data["cooking_time"],
                },
            )
            if was_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"  [CREATED] Recipe: '{recipe.title}'"))
            else:
                self.stdout.write(f"  [SKIP] Already exists: '{recipe.title}'")

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            f"Done! {created} new recipe(s) created.\n"
            f"Demo login  ->  username: {username}  /  password: {password}"
        ))

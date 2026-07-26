import random

# A simple dictionary to track user points: {user_id: points}
# Everyone starts with 100 points for testing!
user_points = {}

def get_points(user_id):
    if user_id not in user_points:
        user_points[user_id] = 100  # Starting balance
    return user_points[user_id]

@bot.command()
async def coinflip(ctx, choice: str, amount: int):
    choice = choice.lower()
    
    # Validate the choice
    if choice not in ["heads", "tails"]:
        await ctx.send("Please choose either **heads** or **tails**! Example: `!coinflip heads 50`")
        return
        
    # Validate the bet amount
    if amount <= 0:
        await ctx.send("You must bet a positive amount of points.")
        return

    user_id = ctx.author.id
    current_balance = get_points(user_id)

    # Check if the user has enough points
    if current_balance < amount:
        await ctx.send(f"❌ You don't have enough points to bet {amount}! You currently have **{current_balance}** points. Earn more before flipping again.")
        return

    # Flip the coin (Randomly pick heads or tails)
    outcome = random.choice(["heads", "tails"])

    if choice == outcome:
        # Win: Add the bet amount (so they get double their bet back: original + winnings)
        user_points[user_id] += amount
        new_balance = user_points[user_id]
        await ctx.send(f"🪙 It landed on **{outcome}**! You won **{amount}** points! 🎉 Your new balance is **{new_balance}** points.")
    else:
        # Lose: Subtract the bet amount
        user_points[user_id] -= amount
        new_balance = user_points[user_id]
        await ctx.send(f"🪙 It landed on **{outcome}**... You lost **{amount}** points. 😢 Your new balance is **{new_balance}** points.")

# Optional helper command to check points
@bot.command()
async def points(ctx):
    balance = get_points(ctx.author.id)
    await ctx.send(f"💰 You currently have **{balance}** points.")
import os
bot.run(os.getenv('TOKEN'))

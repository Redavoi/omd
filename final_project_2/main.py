import logging
import os
import random
from copy import deepcopy

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes, ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logging.getLogger('httpx').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Environment variables
TOKEN = os.getenv('TG_TOKEN')

# Game constants
FREE_SPACE = '.'
CROSS = 'X'
ZERO = 'O'
DEFAULT_STATE = [[FREE_SPACE for _ in range(3)] for _ in range(3)]

# States for conversation
CONTINUE_GAME, FINISH_GAME = range(2)

# Helper function to get default state of the game
def get_default_state():
    """Helper function to get default state of the game"""
    return deepcopy(DEFAULT_STATE)


# Function to generate the game keyboard
def generate_keyboard(state):
    """Generate tic tac toe keyboard 3x3 (telegram buttons)"""
    return [
        [InlineKeyboardButton(state[r][c], callback_data=f'{r}{c}')
         for c in range(3)]
        for r in range(3)
    ]

# Function to start the game
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    context.user_data['keyboard_state'] = get_default_state()
    keyboard = generate_keyboard(context.user_data['keyboard_state'])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("X (your) turn! Please, put X to the free place", reply_markup=reply_markup)
    return CONTINUE_GAME

# Function to end the game
async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ends the game."""
    query = update.callback_query
    await query.answer()  # Acknowledge the callback query

    context.user_data['keyboard_state'] = get_default_state()
    await query.edit_message_text("Game ended. Type /start to play again.")
    return ConversationHandler.END


# Function to check if a player has won
def won(state):
    """Check if crosses or zeros have won the game"""
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] != FREE_SPACE or \
           state[0][i] == state[1][i] == state[2][i] != FREE_SPACE:
            return True
    if state[0][0] == state[1][1] == state[2][2] != FREE_SPACE or \
       state[0][2] == state[1][1] == state[2][0] != FREE_SPACE:
        return True
    return False

# Function for the main game processing
async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Main processing of the game"""
    query = update.callback_query
    await query.answer()

    # Retrieve the position from the callback data
    row, col = int(query.data[0]), int(query.data[1])
    state = context.user_data['keyboard_state']

    # Player's move
    if state[row][col] == FREE_SPACE:
        state[row][col] = CROSS

        # Check for player's win or draw
        if won(state):
            keyboard = generate_keyboard(state)
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.message.edit_text("Your turn!", reply_markup=reply_markup)
            await query.message.reply_text("You win!")
            return FINISH_GAME
        elif not any(FREE_SPACE in row for row in state):
            keyboard = generate_keyboard(state)
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.message.edit_text("Your turn!", reply_markup=reply_markup)
            await query.message.reply_text("It's a draw!")
            return FINISH_GAME

        # AI's move
        empty_cells = [(r, c) for r in range(3) for c in range(3) if state[r][c] == FREE_SPACE]
        if empty_cells:
            ai_row, ai_col = random.choice(empty_cells)
            state[ai_row][ai_col] = ZERO

            # Check AI win
            if won(state):
                keyboard = generate_keyboard(state)
                reply_markup = InlineKeyboardMarkup(keyboard)
                await query.message.edit_text("AI's turn!", reply_markup=reply_markup)
                await query.message.reply_text("AI wins!")
                return FINISH_GAME

        # Update keyboard
        keyboard = generate_keyboard(state)
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text("Your turn!", reply_markup=reply_markup)
        return CONTINUE_GAME
    else:
        await query.message.reply_text("This cell is already occupied. Choose another one.")
        return CONTINUE_GAME


# Setup conversation handler with the states CONTINUE_GAME and FINISH_GAME
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        CONTINUE_GAME: [CallbackQueryHandler(game, pattern='^[0-2][0-2]$')],
        FINISH_GAME: [CallbackQueryHandler(end, pattern='^[0-2][0-2]$')]
    },
    fallbacks=[CommandHandler('start', start)]
)

# Create the Application and pass it your bot's token
application = Application.builder().token(TOKEN).build()

# Add ConversationHandler to the application
application.add_handler(conv_handler)

# Run the bot until the user presses Ctrl-C
application.run_polling()

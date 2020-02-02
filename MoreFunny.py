tuple1 = (
    'these  comments from the failed republican candidate for governor of new york in 2010, #carlpaladino.  ',
    'comments', 'failed')

import random
import re

funny = ['aardvark', 'abacus', 'abundance', 'ache', 'acupuncture',
         'airbrush', 'alien', 'anagram', 'angle', 'amazing', 'ankle',
         'alphabet', 'antenna', 'aqua', 'asphalt', 'bacon', 'banana',
         'bangles', 'banjo', 'bankrupt', 'bar', 'barracuda', 'basket',
         'beluga', 'binder', 'birthday', 'bisect', 'blizzard', 'blunderbuss',
         'boa', 'bog', 'bounce', 'broomstick', 'brought', 'bubble',
         'budgie', 'bug', 'bug-a-boo', 'bugger', 'buff', 'burst', 'butter',
         'buzz', 'cabana', 'cake', 'calculator', 'camera', 'candle',
         'carnival', 'carpet', 'casino', 'cashew', 'caterpillar', 'catfish', 'ceiling',
         'celery', 'chalet', 'chalk', 'chart', 'cheddar', 'chesterfield',
         'chicken', 'chinchilla', 'chit-chat', 'chocolate', 'chowder', 'coal',
         'compass', 'compress', 'computer', 'conduct', 'contents', 'cookie',
         'copper', 'corduroy', 'cow', 'cracker', 'crackle', 'croissant',
         'cube', 'cupcake', 'curly', 'curtain', 'cushion', 'cuticle',
         'daffodil', 'delicious', 'dictionary', 'dimple',
         'disk', 'disco duck', 'dodo', 'dolphin', 'donuts',
         'dracula', 'duct tape', 'effigy', 'egad', 'elastic', 'elephant',
         'encasement', 'erosion', 'eyelash', 'fabulous', 'fantastic',
         'feather', 'falafel', 'fetish', 'financial', 'finger', 'finite',
         'fish', 'fizzle', 'fizzy', 'flame', 'flash', 'flavour', 'flick',
         'flock', 'flour', 'flower', 'foamy', 'foot', 'fork', 'fritter',
         'fudge', 'fungus', 'funny', 'fuse', 'fusion', 'fuzzy', 'garlic',
         'gelatin', 'gelato', 'globe', 'glitter', 'glossy',
         'groceries', 'goulashes', 'guacamole', 'gumdrop', 'haberdashery',
         'hamster', 'happy', 'highlight', 'hippopotamus', 'hobbit', 'hold',
         'hooligan', 'hydrant', 'icicles', 'implode', 'implosion',
         'indeed', 'issue', 'itchy', 'jell-o', 'jewel', 'jump', 'kabob',
         'kasai', 'kite', 'kiwi', 'ketchup', 'knob', 'laces', 'lacy',
         'laughter', 'laundry', 'leaflet', 'legacy', 'leprechaun', 'lollypop',
         'lumberjack', 'macadamia', 'magenta', 'magic', 'magnanimous',
         'mango', 'margarine', 'massimo', 'mechanical', 'medicine', 'meh',
         'melon', 'meow', 'mesh', 'metric', 'microphone', 'minnow', 'mitten',
         'mozzarella', 'muck', 'mumble', 'mushy', 'mustache',
         'noodle', 'nostril', 'nuggets', 'oatmeal', 'oboe', 'o\'clock',
         'octopus', 'odour', 'ointment', 'olive', 'optic', 'overhead', 'ox',
         'oxen', 'pajamas', 'pancake', 'paper', 'paprika',
         'parmesan', 'pasta', 'pattern', 'pecan', 'peek-a-boo', 'pen',
         'pepper', 'pepperoni', 'peppermint', 'perfume', 'periwinkle',
         'photograph', 'pie', 'pierce', 'pillow', 'pineapple',
         'pistachio', 'plush', 'polish', 'pompom', 'poodle', 'pop',
         'popsicle', 'prism', 'prospector', 'prosper', 'pudding', 'puppet',
         'puzzle', 'query', 'radish', 'rainbow', 'ribbon', 'rotate',
         'salami', 'sandwich', 'saturday', 'saturn', 'saxophone', 'scissors',
         'scooter', 'scrabbleship', 'scrunchie', 'scuffle', 'shadow',
         'sickish', 'silicone', 'slippery', 'smash', 'smooch', 'snap',
         'snooker', 'socks', 'soy', 'spaghett','spaghetti', 'sparkle', 'spatula',
         'spiral', 'splurge', 'spoon', 'sprinkle', 'square', 'squiggle',
         'squirrel', 'statistics', 'stuffing', 'sticky', 'sugar',
         'sunshine', 'super', 'swirl', 'taffy', 'tangy', 'tape', 'tat',
         'telephone', 'television', 'thinkable', 'tip', 'tuft',
         'toga', 'trestle', 'tulip', 'turnip', 'turtle', 'tusks',
         'ultimate', 'unicycle', 'unique', 'uranus', 'vegetable', 'waddle',
         'waffle', 'wallet', 'walnut', 'wagon', 'window', 'whatever',
         'whimsical', 'wobbly', 'yellow', 'zap', 'zebra', 'zigzag', 'zip',
         ]

print(tuple1)
data = tuple1[0]
for i in range(len(tuple1) - 1):
    foul = tuple1[i+1]
    foul_replace = (' '.join(random.sample(funny, random.randint(2, 2))))
    print(foul_replace)
    if foul in data:
        foul_replace_hashtag = '#' + foul_replace.replace(" ", '_')
        data = re.sub('#{0}'.format(foul), foul_replace_hashtag, data)
        data = data.replace(foul, foul_replace)
        print(data)

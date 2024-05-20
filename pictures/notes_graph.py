import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# Load the xkcd script font, which has to be downloaded first from https://github.com/ipython/xkcd-font
font_path = '/usr/share/fonts/truetype/xkcd-script/xkcd-script.ttf'  # Ensure this path is correct
font_prop = fm.FontProperties(fname=font_path)

#toggle xkcd styling
plt.xkcd()

fig, ax = plt.subplots(1,figsize = (4,4))
#ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylabel('shareability', fontproperties=font_prop, fontsize = 18)
# Customize x-tick labels with the xkcd font
ax.set_xticks(ticks=[1, 3], labels=['short-time', 'long-time'], fontproperties=font_prop, fontsize = 18)
ax.set_xlim(0.5,3.5)    
ax.set_ylim(0.5,3.5)  # Set y-axis limits to ensure text is visible

# Common kwargs for text
text_kwargs = {
    'fontproperties': font_prop,
    'ha': 'center',
    'va': 'center',
    'fontsize': 18
}
ax.text(1, 1, 'Post-its',  **text_kwargs)
ax.text(2, 1.5, 'Notebook', **text_kwargs)
ax.text(3, 3, 'Wiki', **text_kwargs)

fig.tight_layout()
plt.savefig("./notes_graph.svg")
plt.show()    


import matplotlib.pyplot as plt
fig,ax = plt.subplots(figsize=(15,6))

# ax.scatter(batters['avg'],batters['strike_rate'],color='red',marker='+')
# ax.set_title('Something')
# ax.set_xlabel('Avg')
# ax.set_ylabel('Strike Rate')

# # fig.show()

# fig, ax = plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(10,6))

# ax[0].scatter(batters['avg'],batters['strike_rate'],color='red')
# ax[1].scatter(batters['avg'],batters['runs'])

# ax[0].set_title('Avg Vs Strike Rate')
# ax[0].set_ylabel('Strike Rate')


# ax[1].set_title('Avg Vs Runs')
# ax[1].set_ylabel('Runs')
# ax[1].set_xlabel('Avg')

# fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(10,10))

# ax[0,0].
# ax[0,1].scatter(batters['avg'],batters['runs'])
# ax[1,0].hist(batters['avg'])
# ax[1,1].hist(batters['runs'])

# fig = plt.figure()

# ax1 = fig.add_subplot(2,2,1)
# ax1.scatter(batters['avg'],batters['strike_rate'],color='red')

# ax2 = fig.add_subplot(2,2,2)
# ax2.hist(batters['runs'])

# ax3 = fig.add_subplot(2,2,3)
# ax3.hist(batters['avg'])


# batters

# fig = plt.figure()

# ax = plt.subplot(projection='3d')

# ax.scatter3D(batters['runs'],batters['avg'],batters['strike_rate'],marker='+')
# ax.set_title('IPL batsman analysis')

# ax.set_xlabel('Runs')
# ax.set_ylabel('Avg')
# ax.set_zlabel('SR')


x = [0,1,5,25]
y = [0,10,13,0]
z = [0,13,20,9]

fig = plt.figure()

ax = plt.subplot(projection='3d')

ax.scatter3D(x,y,z,s=[100,100,100,100])
ax.plot3D(x,y,z,color='red')


fig = plt.figure(figsize=(12,8))

ax = plt.subplot(projection='3d')

p = ax.plot_surface(xx,yy,z,cmap='viridis')
fig.colorbar(p)
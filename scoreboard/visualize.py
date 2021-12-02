import json,datetime
import matplotlib.pyplot as plt

OFFSET = int((datetime.datetime(2021,12,1)-datetime.datetime(1970,1,1)).total_seconds())
MARKERS = 'DXos'
MARKERSIZES = [5,7,5,5]
COLORS = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
UK = ['MrGuenst']

scores = json.load(open('623705.json'))['members']
results = {}
for x in scores.values():
    name = x['name']
    res = {}
    for day,submissions in x['completion_day_level'].items():
        d = int(day)
        res[d] = (
            (int(submissions['1']['get_star_ts'])-OFFSET)/60/60-24*(d-1)+(1 if name not in UK else 0) if '1' in submissions else None,
            (int(submissions['2']['get_star_ts'])-OFFSET)/60/60-24*(d-1)+(1 if name not in UK else 0) if '2' in submissions else None
        )
    results[str(name)] = res
    print(str(name), ','.join('{}:({},{})'.format(
        d,
        '{}:{}:{}'.format(int(s1//1), int(((s1*60)%60)//1), int(((s1*3600)%60)//1)) if s1 is not None else "None",
        '{}:{}:{}'.format(int(s2//1), int(((s2*60)%60)//1), int(((s2*3600)%60)//1)) if s2 is not None else "None"
    ) for d,(s1,s2) in sorted(res.items())))

fig = plt.figure(figsize=(15,8))
ax = fig.gca()
ax.set_xlim((6,24))
ax.set_ylim((0,26))
for i in range(1,26):
    ax.plot([6,24],[i,i], color = 'k')
for i,(name,res) in enumerate(sorted(results.items(), key = lambda x : x[0].lower())):
    if not res: continue
    for j in range(2):
        xs,ys = zip(*[(x[j],d) for d,x in sorted(res.items()) if x[j] is not None])
        color = COLORS[i%len(COLORS)]
        marker = MARKERS[i//len(COLORS)]
        markersize = MARKERSIZES[i//len(COLORS)]
        ax.plot(xs, ys, marker = marker, markersize = markersize, linestyle = '', color = color, label = name if j == 0 else None, zorder = 10)
        ax.plot(xs, ys, color = color, linestyle = '--' if j == 1 else '-', alpha = .2)

box = ax.get_position()
ax.set_position([box.x0 + .12*box.width, box.y0, .95*box.width, box.height])
fig.legend(loc = 'center left', framealpha=1, bbox_to_anchor = (.02,.5))

xticks = [6,12,18,24]
yticks = range(1,26)
ax.set_xticks(xticks)
ax.set_xticklabels(map(lambda x : '{}:00'.format(x%24), xticks))
ax.set_yticks(yticks)
ax.set_yticklabels(map(lambda y : 'Day {}'.format(y), yticks))
ax.set_xlabel('Local time')
fig.savefig('scores.png')
plt.show()

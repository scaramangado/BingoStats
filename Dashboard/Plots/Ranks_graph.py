from Dashboard.Plots.Layout import get_graph_layout
import plotly.graph_objs as go
import Utils

#### GRAPH 1 - Ranks ####

def get_ranks_graph(player=None):
    data = []

    if player:
        races = player.select_races()
        points = [Data_point(race) for race in races]

        dates          = [point.date          for point in points]
        times          = [point.scatter_time  for point in points]
        relative_ranks = [point.relative_rank for point in points]
        markers        = [point.marker        for point in points]

        data = [go.Scatter(
                x=dates,
                y=times,
                text=markers,
                mode='markers',
                opacity=1,
                marker={
                    'size': 12,
                    'line': {'width': 0.5, 'color': 'black'},
                    'color': relative_ranks,
                    'showscale':False
                },
                hoverinfo='text'
        )]


    return {
        'data': data,
        'layout': get_graph_layout(title='Bingo races', height=650)
    }


class Data_point:

    def __init__(self, race):
        self.date = race.date
        self.relative_rank = self.relative_rank(race)
        time = race.time.total_seconds()
        self.scatter_time, human_time = Utils.convert_to_human_readable_time(time)

        self.marker = self.date.strftime('%b %d') + '<br>' + race.type + '<br>'+str(human_time)+'<br>rank: '+str(race.rank)+'/'+str(race.total_players)

    def relative_rank(self, race):
        return (1 / (race.total_players - 1)) * (race.rank - 1)
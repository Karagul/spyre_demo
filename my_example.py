from spyre import server
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.xkcd();

class SimpleApp(server.App):
	title = "Educational Spending by State"
	inputs = [{
		"type": "dropdown",
		"key": "state1",
		"label": "State 1",
		'options': [
            {"label": "Alabama", "value": "ALABAMA"},
            {"label": "Alaska", "value": "ALASKA"},
            {"label": "Arizona", "value": "ARIZONA"},
            {"label": "Arkansas", "value": 'ARKANSAS'},
            {"label": "California", "value": "CALIFORNIA"},
            {"label": "Colorado", "value": "COLORADO"},
            {"label": "Connecticut", "value": "CONNECTICUT"},
            {"label": "Delaware", "value": "DELAWARE"},
            {"label": "Florida", "value": "FLORIDA"},
            {"label": "Georgia", "value": "GEORGIA"},
            {"label": "Hawaii", "value": "HAWAII"},
            {"label": "Idaho", "value": "IDAHO"},
            {"label": "Illinois", "value": "ILLINOIS"},
            {"label": "Indiana", "value": "INDIANA"},
            {"label": "Iowa", "value": "IOWA"},
            {"label": "Kansas", "value": "KANSAS"},
            {"label": "Kentucky", "value": "KENTUCKY"},
            {"label": "Louisiana", "value": "LOUISIANA"},
            {"label": "Maine", "value": "MAINE"},
            {"label": "Maryland", "value": "MARYLAND"},
            {"label": "Massachusetts", "value": "MASSACHUSETTS"},
            {"label": "Michigan", "value": "MICHIGAN"},
            {"label": "Minnesota", "value": "MINNESOTA"},
            {"label": "Mississippi", "value": "MISSISSIPPI"},
            {"label": "Missouri", "value": "MISSOURI"},
            {"label": "Montana", "value": "MONTANA"},
            {"label": "Nebraska", "value": "NEBRASKA"},
            {"label": "Nevada", "value": "NEVADA"},
            {"label": "New Hampshire", "value": "NEW_HAMPSHIRE"},
            {"label": "New Jersey", "value": "NEW_JERSEY"},
            {"label": "New Mexico", "value": "NEW_MEXICO"},
            {"label": "New York", "value": "NEW_YORK"},
            {"label": "North Carolina", "value": "NORTH_CAROLINA"},
            {"label": "North Dakota", "value": "NORTH_DAKOTA"},
            {"label": "Ohio", "value": "OHIO"},
            {"label": "Oklahoma", "value": "OKLAHOMA"},
            {"label": "Oregon", "value": "OREGON"},
            {"label": "Pennsylvania", "value": "PENNSYLVANIA"},
            {"label": "Rhode Island", "value": "RHODE_ISLAND"},
            {"label": "South Carolina", "value": "SOUTH_CAROLINA"},
            {"label": "South Dakota", "value": "SOUTH_DAKOTA"},
            {"label": "Tennessee", "value": "TENNESSEE"},
            {"label": "Texas", "value": "TEXAS"},
            {"label": "Utah", "value": "UTAH"},
            {"label": "Vermont", "value": "VERMONT"},
            {"label": "Virginia", "value": "VIRGINIA"},
            {"label": "Washington", "value": "WASHINGTON"},
            {"label": "Washington DC", "value": 'DISTRICT_OF_COLUMBIA'},
            {"label": "West Virginia", "value": "WEST_VIRGINIA"},
            {"label": "Wisconsin", "value": "WISCONSIN"},
            {"label": "Wyoming", "value": "WYOMING"}],
            'action_id': 'button1'
            },
            {
		"type": "dropdown",
		"key": "state2",
		"label": "State 2",
		'options': [
            {"label": "Alabama", "value": "ALABAMA"},
            {"label": "Alaska", "value": "ALASKA"},
            {"label": "Arizona", "value": "ARIZONA"},
            {"label": "Arkansas", "value": 'ARKANSAS'},
            {"label": "California", "value": "CALIFORNIA"},
            {"label": "Colorado", "value": "COLORADO"},
            {"label": "Connecticut", "value": "CONNECTICUT"},
            {"label": "Delaware", "value": "DELAWARE"},
            {"label": "Florida", "value": "FLORIDA"},
            {"label": "Georgia", "value": "GEORGIA"},
            {"label": "Hawaii", "value": "HAWAII"},
            {"label": "Idaho", "value": "IDAHO"},
            {"label": "Illinois", "value": "ILLINOIS"},
            {"label": "Indiana", "value": "INDIANA"},
            {"label": "Iowa", "value": "IOWA"},
            {"label": "Kansas", "value": "KANSAS"},
            {"label": "Kentucky", "value": "KENTUCKY"},
            {"label": "Louisiana", "value": "LOUISIANA"},
            {"label": "Maine", "value": "MAINE"},
            {"label": "Maryland", "value": "MARYLAND"},
            {"label": "Massachusetts", "value": "MASSACHUSETTS"},
            {"label": "Michigan", "value": "MICHIGAN"},
            {"label": "Minnesota", "value": "MINNESOTA"},
            {"label": "Mississippi", "value": "MISSISSIPPI"},
            {"label": "Missouri", "value": "MISSOURI"},
            {"label": "Montana", "value": "MONTANA"},
            {"label": "Nebraska", "value": "NEBRASKA"},
            {"label": "Nevada", "value": "NEVADA"},
            {"label": "New Hampshire", "value": "NEW_HAMPSHIRE"},
            {"label": "New Jersey", "value": "NEW_JERSEY"},
            {"label": "New Mexico", "value": "NEW_MEXICO"},
            {"label": "New York", "value": "NEW_YORK"},
            {"label": "North Carolina", "value": "NORTH_CAROLINA"},
            {"label": "North Dakota", "value": "NORTH_DAKOTA"},
            {"label": "Ohio", "value": "OHIO"},
            {"label": "Oklahoma", "value": "OKLAHOMA"},
            {"label": "Oregon", "value": "OREGON"},
            {"label": "Pennsylvania", "value": "PENNSYLVANIA"},
            {"label": "Rhode Island", "value": "RHODE_ISLAND"},
            {"label": "South Carolina", "value": "SOUTH_CAROLINA"},
            {"label": "South Dakota", "value": "SOUTH_DAKOTA"},
            {"label": "Tennessee", "value": "TENNESSEE"},
            {"label": "Texas", "value": "TEXAS"},
            {"label": "Utah", "value": "UTAH"},
            {"label": "Vermont", "value": "VERMONT"},
            {"label": "Virginia", "value": "VIRGINIA"},
            {"label": "Washington", "value": "WASHINGTON"},
            {"label": "Washington DC", "value": 'DISTRICT_OF_COLUMBIA'},
            {"label": "West Virginia", "value": "WEST_VIRGINIA"},
            {"label": "Wisconsin", "value": "WISCONSIN"},
            {"label": "Wyoming", "value": "WYOMING"}],
            'action_id': 'button1'
            }
            ]
	tabs = ["Plot", "Table"]

	controls = [
	{
	'type': 'hidden',
	'id': 'button1'
	},
	{
	'type': 'button',
	'id': 'button2',
	'label': 'download?'
	}
	]

	outputs = [{
	'type': 'table',
	'id': 'table_id',
	'control_id': 'button1',
	'tab': 'Table',
	'on_page_load': True
	},
	{
	'type': 'plot',
	'id': 'plot_id',
	'control_id': 'button1',
	'tab': 'Plot',
	'on_page_load': True
	},

	{
	'type': 'download',
	'id': 'download_id',
	'control_id': 'button2',
	'on_page_load': False
	}
	]

	def getData(self, params):
	    df = pd.read_csv('states_all.csv')
	    df['Spent per Student'] = df['TOTAL_EXPENDITURE'] / df['GRADES_ALL_G']
	    state1 =  params['state1']
	    state2 = params['state2']
	    df.set_index('YEAR', inplace = True)
	    df1 = pd.DataFrame()
	    df1[state1] = df[df['STATE'] == state1]['Spent per Student']
	    df1[state2] = df[df['STATE'] == state2]['Spent per Student']
	    df1.reset_index(inplace = True)
	    return df1

	def getPlot(self, params):
	    df2 = self.getData(params)
	    df2.set_index('YEAR', inplace = True)
	    fig = df2.plot(kind = 'line', figsize = (12, 8))
	    plt.ylabel('Spent Per Student')
	    plt.title(f'{params["state1"].title()} vs {params["state2"].title()} Spent per Student by Year')
	    return fig

	def getCustomCSS(self):
		css = (
		    "body { background-image: "
		    "url('https://github.com/adamhajari/spyre/blob/master/"
		    "examples/screenshots/jungle-cruise-gallery06.jpg?raw=true');}"
		)
		return css
app = SimpleApp()
app.launch()
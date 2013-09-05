import sublime, sublime_plugin

class InvertSelectionCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		currentSelections = self.view.sel()
		cursor = 0
		unselectRegions = []
		for selection in currentSelections:
			if(selection.begin() > cursor):
				unselectRegions.append(sublime.Region(cursor,selection.begin()))
			cursor = selection.end()
		if(cursor < self.view.size()):
			unselectRegions.append(sublime.Region(cursor,self.view.size()))
		self.view.sel().clear()
		for unselectRegion in unselectRegions:
			self.view.sel().add(unselectRegion)

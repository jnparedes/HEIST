class ExplanationsModule:

	def __init__(self, qam, services, user, styles):
		self._qam = qam
		self._services = services
		self._user = user
		self._styles = styles
		self._chosen_styles = []
		self._chosen_sources = []

	def explain(self, answer, query):
		explanation = []
		for style_visitor in self._chosen_styles:
			for source in self._chosen_source:
				source.accept(style_visitor)

			style = style_visitor.create()
			single_explanation = style.explain(answer, query)
			explanation.append(single_explanation)

		return explanation


	def get_sources(self):
		return self._qam.get_sources()

	def set_chosen_sources(self, chosen_sources):
		self._chosen_sources = chosen_sources

	def get_styles(self):
		return self._styles

	def set_chosen_styles(self, chosen_styles):
		self._chosen_styles = chosen_styles


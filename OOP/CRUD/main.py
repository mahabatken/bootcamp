from views_mixns import *

class Post(CreateMixin, ReadMixins, UpdateMixin, SaveMixin):
    pass

class Comment(CreateMixin, ReadMixins, UpdateMixin, SaveMixin):
    pass
class Like(CreateMixin, ReadMixins, UpdateMixin, SaveMixin):
    pass
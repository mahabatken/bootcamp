
from CRUD.search import search_object
import json
class CReateMixin:
       def _get_or_set_objects(self):
        try:
            if self.objects and self.id:
                pass
        except(NameError, AttributeError):
            self._objects = []
            self._id = 0 

        def __init__(self) -> None:
            self._get_or_set_objects()

        def create (self,**kwargs):
            self._id +=1
            obj = dict(id= self._id, **kwargs) 
            self._objects.append(obj)
            print({'status': '201 Created', 'msg': obj['title']})
            self._save()
        return {'status': '201 Created', 'msg': obj['title']}

class ReadMixins:
     def list(self):
        res = [{"id":x['id'], 'title':x['title'], 'price' :x['price']}for x in self._objects]
        print({'status': 200, 'msg': res })
        return  {'status': 200, 'msg': res }
    
@search_object
    def detail(self, id , **kwargs):
        product = kwargs['object_']
        return {'status': '20 oK', 'msg': product }
        
class UpdateMixin:
    @search_object
    def update(self, id, **kwargs):
        product = kwargs.pop('object_')
        product.update(**kwargs)
        self._save()
        return {'status': '206 Updated'}
class DeleteMixin:
    @search_object
    def delete(self,id, **kwargs):
        product = kwargs['object_']
        self._objects.remove(product)
        self._save()
        return {'status': '202 No Content'}
class SaveMixin:
     def _save(self):
        with open('data.json', 'w') as file:
            json.dump(self._objects, file, indent=4)
        return 'saved!'


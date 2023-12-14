from flask import Blueprint, render_template 



#need to instantiate our Blueprint class
catalog = Blueprint('catalog', __name__, template_folder='catalog_templates' )


#use site object to create our routes
@catalog.route('/catalog')
def createcatalog():
    return render_template('catalog.html') #looking inside our template_folder (site_templates) to find our catalog.html file
import os
from functools import reduce

package_name = 'piculator-system'
name = 'piculator-system'
desp = 'Piculatorize your raspberry pi zero'
version = input('Please input version:')
package_path = f'{package_name}_{version}'
os.makedirs(f"{package_path}/DEBIAN", exist_ok=True)
dependencies = {
    'piculator-client': '=1.0',
    'piculator-localhost': '=1.0',
    'piculator-mu-editor': '=1.0.3',
    'piculator-plym-splash': '=1.0',
    'piculator-sagemath': '=9.2',
    'piculator-sage-documentation-en': '=1.0',
    'piculator-chinese-support': '=1.0',
    'piculator-static-gamma': '=1.0',
    'piculator-static-icons': '=1.0.1',
    'piculator-static-stopwatch': '=1.0',
    'piculator-xmodkey': '=1.0',
}
depends = reduce(lambda x,y:x+y,\
    map(lambda z: z+ \
        (f'{z} ({dependencies[z]}), ' if dependencies[z] is not None else ', '),\
        dependencies.keys()))[:-2]
control_content = f'''Package: {package_name}
Architecture: all
Name: {name}
Description: {desp}
Version: {version}
Section: base
Depends: {depends}
Author: Piculator Development Team <piculator@protonmail.com>
Maintainer: Piculator Development Team <piculator@protonmail.com>
HomePage: https://github.com/piculator/{package_name}-software
'''
ctl_file = open(f'{package_path}/DEBIAN/control', mode='w+')
ctl_file.write(control_content)
ctl_file.close()
os.system(f'dpkg-deb -b {package_path}')

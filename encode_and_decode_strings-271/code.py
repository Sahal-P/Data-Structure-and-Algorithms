import time

def encodedecode(arr):
    encoded = ""
    for i in arr:
        lent = len(i)
        encoded += f"{lent}#{i}"
    return encoded


def decodecode(encoded):
    decoded = []
    num = ""
    for t, j in enumerate(encoded):
        if j.isdigit():
            num += j
        if j == "#":
            word = ""
            for k in range(1, int(num) + 1):
                word += encoded[t + k]
            decoded.append(word)
            word = ""
            num = ""
    return decoded

#converting string to arr
def stringtoarr(stri):
    arr = []
    word = ""
    for i in stri:
        if i != " ":
            word += i
        if i == " ":
            arr.append(word)
            word = ""
            continue
    arr.append(word)
    return arr


string = "At vero eos et Ut venenatis magna hendrerit, dignissim sem ac, feugiat velit. Nulla mattis semper ultricies. Fusce diam ligula, tincidunt ac justo nec, eleifend aliquet dolor. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla id arcu placerat, sodales libero at, commodo mauris. Vivamus nec placerat elit. Suspendisse feugiat nec erat ut consectetur. Sed iaculis velit vitae lorem consequat consectetur. Vestibulum consectetur, augue ut dapibus imperdiet, neque diam luctus justo, sit amet sagittis nulla metus a nulla. Pellentesque eu lorem hendrerit, venenatis lacus vel, egestas metus. Fusce sollicitudin sem nulla, vitae posuere ipsum placerat sit amet. Nullam mattis euismod tristique. Fusce consectetur porttitor odio sollicitudin sollicitudin Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Proin ornare nisi et lorem condimentum, eget aliquet risus fringilla. Nunc ut dignissim neque, et interdum arcu. Sed dignissim semper purus, vehicula consectetur mi porttitor quis. Donec ultrices convallis volutpat. Morbi nec turpis aliquet orci eleifend sagittis. Donec imperdiet dolor eu nisl commodo, ut ullamcorper leo porttitor. Donec elementum mauris mauris, vitae condimentum lorem volutpat vel. Quisque in augue in justo fermentum pretium ut ac orci. Quisque sit amet velit cursus, luctus massa a, semper odio. Quisque eu eros nec quam egestas finibus a a lorem Sed dapibus ac eros et sollicitudin. Ut ac nisi tempus libero dapibus ultrices. Integer lacus mauris, commodo non fringilla ac, congue sit amet dolor. Duis at nisl sed ipsum sagittis venenatis at ut nunc. Sed pretium consectetur massa vitae lacinia. Donec nisi neque, facilisis non porttitor feugiat, mollis in tortor. Fusce sit amet ultrices tellus. Integer nec fermentum ex. Pellentesque tincidunt neque eget maximus efficitur. Morbi pharetra nibh vitae lorem bibendum facilisis. Vivamus quis condimentum odio. Nulla et euismod massa. Ut feugiat, risus nec consectetur accumsan, nibh lorem auctor ligula, suscipit pellentesque nisl lorem id nibh. Sed ullamcorper, libero id imperdiet accumsan, velit urna pellentesque tellus, molestie pellentesque eros libero at tellus. Pellentesque lorem libero, condimentum congue lacus quis, convallis vestibulum ipsum Sed dapibus ac eros et sollicitudin. Ut ac nisi tempus libero dapibus ultrices. Integer lacus mauris, commodo non fringilla ac, congue sit amet dolor. Duis at nisl sed ipsum sagittis venenatis at ut nunc. Sed pretium consectetur massa vitae lacinia. Donec nisi neque, facilisis non porttitor feugiat, mollis in tortor. Fusce sit amet ultrices tellus. Integer nec fermentum ex. Pellentesque tincidunt neque eget maximus efficitur. Morbi pharetra nibh vitae lorem bibendum facilisis. Vivamus quis condimentum odio. Nulla et euismod massa. Ut feugiat, risus nec consectetur accumsan, nibh lorem auctor ligula, suscipit pellentesque nisl lorem id nibh. Sed ullamcorper, libero id imperdiet accumsan, velit urna pellentesque tellus, molestie pellentesque eros libero at tellus. Pellentesque lorem libero, condimentum congue lacus quis, convallis vestibulum ipsum Sed dapibus ac eros et sollicitudin. Ut ac nisi tempus libero dapibus ultrices. Integer lacus mauris, commodo non fringilla ac, congue sit amet dolor. Duis at nisl sed ipsum sagittis venenatis at ut nunc. Sed pretium consectetur massa vitae lacinia. Donec nisi neque, facilisis non porttitor feugiat, mollis in tortor. Fusce sit amet ultrices tellus. Integer nec fermentum ex. Pellentesque tincidunt neque eget maximus efficitur. Morbi pharetra nibh vitae lorem bibendum facilisis. Vivamus quis condimentum odio. Nulla et euismod massa. Ut feugiat, risus nec consectetur accumsan, nibh lorem auctor ligula, suscipit pellentesque nisl lorem id nibh. Sed ullamcorper, libero id imperdiet accumsan, velit urna pellentesque tellus, molestie pellentesque eros libero at tellus. Pellentesque lorem libero, condimentum congue lacus quis, convallis vestibulum ipsum Sed dapibus ac eros et sollicitudin. Ut ac nisi tempus libero dapibus ultrices. Integer lacus mauris, commodo non fringilla ac, congue sit amet dolor. Duis at nisl sed ipsum sagittis venenatis at ut nunc. Sed pretium consectetur massa vitae lacinia. Donec nisi neque, facilisis non porttitor feugiat, mollis in tortor. Fusce sit amet ultrices tellus. Integer nec fermentum ex. Pellentesque tincidunt neque eget maximus efficitur. Morbi pharetra nibh vitae lorem bibendum facilisis. Vivamus quis condimentum odio. Nulla et euismod massa. Ut feugiat, risus nec consectetur accumsan, nibh lorem auctor ligula, suscipit pellentesque nisl lorem id nibh. Sed ullamcorper, libero id imperdiet accumsan, velit urna pellentesque tellus, molestie pellentesque eros libero at tellus. Pellentesque lorem libero, condimentum congue lacus quis, convallis vestibulum ipsum Sed dapibus ac eros et sollicitudin. Ut ac nisi tempus libero dapibus ultrices. Integer lacus mauris, commodo non fringilla ac, congue sit amet dolor. Duis at nisl sed ipsum sagittis venenatis at ut nunc. Sed pretium consectetur massa vitae lacinia. Donec nisi neque, facilisis non porttitor feugiat, mollis in tortor. Fusce sit amet ultrices tellus. Integer nec fermentum ex. Pellentesque tincidunt neque eget maximus efficitur. Morbi pharetra nibh vitae lorem bibendum facilisis. Vivamus quis condimentum odio. Nulla et euismod massa. Ut feugiat, risus nec consectetur accumsan, nibh lorem auctor ligula, suscipit pellentesque nisl lorem id nibh. Sed ullamcorper, libero id imperdiet accumsan, velit urna pellentesque tellus, molestie pellentesque eros libero at tellus. Pellentesque lorem libero, condimentum congue lacus quis, convallis vestibulum ipsum accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure? At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains"


if __name__ == "__main__":
  start = time.time()
  convStr = stringtoarr(string)
  val = encodedecode(convStr)
  val2 = decodecode(val)
  end = time.time()
  print(end - start)

from keras_transformer import get_model, decode
import json

directorio = "./dataset/diccionarios/es_qu/source_token_dict.json"
with open(directorio) as json_file:
    source_token_dict = json.load(json_file)

directorio = "./dataset/diccionarios/es_qu/target_token_dict.json"
with open(directorio) as json_file:
    target_token_dict = json.load(json_file)

directorio = "./dataset/diccionarios/es_qu/target_token_dict_inv.json"
with open(directorio) as json_file:
    target_token_dict_inv = json.load(json_file)


directorio = "./dataset/diccionarios/qu_es/source_token_dict_qu.json"
with open(directorio) as json_file:
    source_token_dict_qu = json.load(json_file)

directorio = "./dataset/diccionarios/qu_es/target_token_dict_qu.json"
with open(directorio) as json_file:
    target_token_dict_qu = json.load(json_file)

directorio = "./dataset/diccionarios/qu_es/target_token_dict_inv_qu.json"
with open(directorio) as json_file:
    target_token_dict_inv_qu = json.load(json_file)


modelEsp = get_model(
    token_num = 16186,
    embed_dim = 32,
    encoder_num = 2,
    decoder_num = 2,
    head_num = 4,
    hidden_dim = 128,
    dropout_rate = 0.05,
    use_same_embed = False,
)
modelEsp.compile('adam', 'sparse_categorical_crossentropy', 'accuracy')

modelQch = get_model(
    token_num = 16186,
    embed_dim = 32,
    encoder_num = 2,
    decoder_num = 2,
    head_num = 4,
    hidden_dim = 128,
    dropout_rate = 0.05,
    use_same_embed = False,
)
modelQch.compile('adam', 'sparse_categorical_crossentropy', 'accuracy')

modelEsp.load_weights('./modelo/traductor_es_qu.h5')
modelQch.load_weights('./modelo/traductor_qu_es.h5')


def traducirEsp(sentence):
  sentence_tokens = [tokens + ['<FIN>', '<RELLENO>'] for tokens in [sentence.split(' ')]]
  try:
    for i in sentence_tokens[0]:
      if i not in source_token_dict:
        source_token_dict.setdefault(i,len(source_token_dict)+1)
        target_token_dict_inv.setdefault(i,len(target_token_dict_inv)+1)
    tr_input = [list(map(lambda x: source_token_dict[x], tokens)) for tokens in sentence_tokens][0]
    decoded = decode(
        modelEsp,
        tr_input,
        start_token = target_token_dict['<INICIO>'],
        end_token = target_token_dict['<FIN>'],
        pad_token = target_token_dict['<RELLENO>']
    )
    decoded = list(map(str, decoded))

    return '{}'.format(' '.join(map(lambda x: target_token_dict_inv[x], decoded[1:-1])))
  except:
    return 'Lo sentimos, no se ha podido traducir'


def traducirQch(sentence):
  sentence_tokens = [tokens + ['<FIN>', '<RELLENO>'] for tokens in [sentence.split(' ')]]
  try:
    for i in sentence_tokens[0]:
      if i not in source_token_dict_qu:
        source_token_dict_qu.setdefault(i,len(source_token_dict_qu)+1)
        target_token_dict_inv_qu.setdefault(i,len(target_token_dict_inv_qu)+1)
    tr_input = [list(map(lambda x: source_token_dict_qu[x], tokens)) for tokens in sentence_tokens][0]
    decoded = decode(
        modelQch,
        tr_input,
        start_token = target_token_dict_qu['<INICIO>'],
        end_token = target_token_dict_qu['<FIN>'],
        pad_token = target_token_dict_qu['<RELLENO>']
    )
    decoded = list(map(str, decoded))

    return '{}'.format(' '.join(map(lambda x: target_token_dict_inv_qu[x], decoded[1:-1])))
  except:
    return 'pampachaykuway, manan kanchu t’ikray'

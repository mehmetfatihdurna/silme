const { MongoClient } = require('mongodb');

async function main(){
  const uri = 'mongodb+srv://<author>:<passwoord>@cluster0.croktut.mongodb.net/?retryWrites=true&w=majority';
  // const uri = 'mongodb://localhost:27017';
  const client = new MongoClient(uri);

  try{
    await client.connect();
    // await listDatabases(client);

    // await createMultipleListing(client,[
    //   {name: 'Sümeyye', summary: 'Uzun',bedrooms: 4,bathrooms: 7},
    //   {name: 'Abdülaziz', summary: 'Uzun',bedrooms: 5,bathrooms: 4}
    // ])

    await updateListingByName(client,'metehan');
    await findOneListingByName(client,'metoskos');
    await deleteOneByeName(client, 'Aziz');

    await findOneListingByName(client,'Aziz');

  }catch(e){
    console.error(e);
  }finally{
    await client.close();
  }


}

main().catch(console.error);


async function deleteOneByeName(client,name){
  const result = await client.db('sample_airbnb').collection('listingsAndReviews').deleteOne({name : {$regex:name,$options: 'i'}});
  console.log(result);
}



async function updateListingByName(client,name){
  const result = await client.db('sample_airbnb').collection('listingsAndReviews').updateOne({name: {$regex: name,$options:'i'}},{$set: {name: 'Metoskos'}})

}


async function findOneListingByName(client,name){
  const cursor = await client.db('sample_airbnb').collection('listingsAndReviews').find({name: {$regex: name,$options: 'i'}});
  const result = await cursor.toArray();
  console.log(result);
}


async function createMultipleListing(client,multipleList){
  const result = await client.db('sample_airbnb').collection('listingsAndReviews').insertMany(multipleList);
  console.log(result.insertedCount +' new listings created with the following id: ' + result.insertedIds);
}


async function createListing(client,newListing){
  const result = await client.db('sample_airbnb').collection('listingsAndReviews').insertOne(newListing);
  console.log('New listing created with the following id: ' + result.insertedId);
}


async function listDatabases(client){
  const databasesList = await client.db().admin().listDatabases();
  console.log('Databases: ');
  databasesList.databases.forEach(db => {
    console.log('- ' + db.name);

  });
}

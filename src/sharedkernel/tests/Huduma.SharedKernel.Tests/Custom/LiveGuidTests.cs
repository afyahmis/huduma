using System;
using Huduma.SharedKernel.Custom;
using NUnit.Framework;

namespace Huduma.SharedKernel.Tests.Custom
{
    [TestFixture]
    public class LiveGuidTests
    {
        [Test]
        public void should_Generate_NewGuid()
        {
            var idA = LiveGuid.NewGuid();
            var idB = LiveGuid.NewGuid();
            Assert.That(idA.ToString(), Is.Not.EqualTo(idB.ToString()));
            Console.WriteLine($"{idA}");
            Console.WriteLine($"{idB}");
        }
    }
}